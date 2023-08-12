import asyncio
import gzip
import json
import logging
import os
from dataclasses import dataclass
from typing import Optional

import httpx
import polling2
from gql import gql
from gql.client import AsyncClientSession, Client
from gql.transport.appsync_auth import AppSyncJWTAuthentication
from gql.transport.appsync_websockets import AppSyncWebsocketsTransport
from rich.console import Console
from rich.progress import Progress, TaskID

from .client import ComputeGraphqlClient, PublicGraphqlClient
from .queries import (
    INPUT_DATA_OBJECT_QUERY,
    JOIN_SUBSCRIPTION,
    OUTPUT_DATA_OBJECT_QUERY,
    POLL_QUERY,
)
from .types import Events


_PLATFORM_CORE_REALTIME_API_HOST = os.environ.get(
    "PLATFORM_CORE_REALTIME_API_HOST",
    "on2v7zovkzeyzp34lgmtzsrgrq.appsync-realtime-api.eu-west-2.amazonaws.com",  # noqa
)


def _build_async_transport(access_token: str):
    """
    Builds and returns an AppSyncWebsocketsTransport
    instance for the given access token.

    :param access_token: The access token to be used for authentication.
    :return: An instance of AppSyncWebsocketsTransport.
    """
    return AppSyncWebsocketsTransport(
        url=f"https://{_PLATFORM_CORE_REALTIME_API_HOST}/graphql",
        auth=AppSyncJWTAuthentication(
            host=_PLATFORM_CORE_REALTIME_API_HOST,
            jwt=f"ensquared::user-token::{access_token}",
        ),
        close_timeout=1,
        connect_args={
            "ping_interval": 2,
            "ping_timeout": 2,
            "close_timeout": 1,
            "timeout": 1,
        },
    )


@dataclass
class Execution:
    _api_key: str
    _compute_client: ComputeGraphqlClient
    _public_client: PublicGraphqlClient

    id: str
    package_object_id: str
    input_object_id: Optional[str] = None
    output_object_id: Optional[str] = None

    @classmethod
    def submit(cls, package: str, *, api_key: str):
        """
        Submits a new execution and initializes an
        Execution instance with the response data.

        :param package: The package to be executed.
        :param api_key: The API key for authentication.
        :return: An instance of the Execution class with the execution data.
        """
        public_client = PublicGraphqlClient(token=api_key)
        compute_client = ComputeGraphqlClient(token=api_key)
        response = compute_client.execute(
            gql(
                """
                    mutation ($package: String!) {
                        submitGraphExecution(package: $package) {
                            id
                            packageObjectId
                        }
                    }
                """
            ),
            variable_values={"package": package},
        )
        return cls(
            _api_key=api_key,
            _public_client=public_client,
            _compute_client=compute_client,
            id=response["submitGraphExecution"]["id"],
            package_object_id=response["submitGraphExecution"]["packageObjectId"],
        )

    def _poll_for_completion(self):
        """
        Polls the current execution for its completion status.

        :return: The response containing the execution status.
        """
        return self._compute_client.execute(POLL_QUERY, variable_values={"id": self.id})

    @staticmethod
    def _is_complete(response):
        """
        Checks if the execution is complete based on the response.

        :param response: The response containing the execution status.
        :return: True if the execution is complete, otherwise False.
        """
        return response["execution"]["status"] in ["SUCCEEDED", "FAILED"]

    def poll_for_completion(self):
        """
        Polls the current execution for completion using the _poll_for_completion method
        and updates the output_object_id when it's completed.
        """
        response = polling2.poll(
            self._poll_for_completion,
            check_success=self._is_complete,
            step=1,
            timeout=3600,
        )

        if response["execution"]["status"] == "FAILED":
            raise Exception("Error")

        self.output_object_id = response["execution"]["outputObjectId"]

    def _get_object_size(self, object_id: str):
        default_size = 1
        object_ = self._public_client.execute(
            INPUT_DATA_OBJECT_QUERY,
            variable_values={"id": object_id},
        )["object"]
        return object_["dataLength"] or default_size

    def _handle_message(
        self,
        message,
        *,
        progress: Progress,
        node_task_map: dict[str, TaskID],
    ):
        message_data_string = message["subscribe"]["data"]
        if message_data_string is not None:
            message = json.loads(message_data_string)
            message_name = message["name"]
            message_data = message["data"]

            if message_name == Events.NodeExecutionSubmitted:
                if "compute::orchestration::end" not in message.get("scopes", []):
                    node_task_map[message_data["node_id"]["value"]] = progress.add_task(
                        f"[cyan]({len(node_task_map)}) Running...",
                        total=self._get_object_size(
                            message_data["input_object_id"]["value"]
                        ),
                    )

            elif message_name == Events.ExecutionCompleted:
                node_id = message_data["node_id"]["value"]
                if node_id in node_task_map:
                    progress.advance(node_task_map[message_data["node_id"]["value"]], 1)

            elif message_name == Events.GraphExecutionExited:
                return True

    async def _join(self, session: AsyncClientSession):
        console = Console()
        node_task_map: dict[str, TaskID] = {}
        with Progress(console=console) as progress:
            async for message in session.subscribe(
                JOIN_SUBSCRIPTION,
                variable_values={"scope": f"compute::execution::{self.id}"},
            ):
                if (
                    result := self._handle_message(
                        message,
                        progress=progress,
                        node_task_map=node_task_map,
                    )
                    is not None
                ):
                    return result

    async def join(self):
        """
        Joins the execution subscription and listens for
        messages. Processes messages as they arrive.
        """
        client = Client(transport=_build_async_transport(self._api_key))

        async with client as session:
            subscription_task = asyncio.create_task(self._join(session))
            done, pending = await asyncio.wait(
                {subscription_task},
                return_when=asyncio.FIRST_COMPLETED,
            )
            if subscription_task in done:
                await client.close_async()
                self.poll_for_completion()
                results = self.get_results()

            for task in pending:
                task.cancel()

            return results

    def get_results(self):
        """
        Retrieves the results of the execution by fetching the output object data.

        :return: A JSON object containing the results of the execution.
        """
        try:
            response = self._public_client.execute(
                OUTPUT_DATA_OBJECT_QUERY,
                variable_values={"id": self.output_object_id},
            )

            return json.loads(
                gzip.decompress(httpx.get(response["object"]["getUrl"]).content).decode(
                    "utf-8"
                )
            )
        except Exception as error:
            logging.error(f"Error retrieving results: {error}")
            return None
