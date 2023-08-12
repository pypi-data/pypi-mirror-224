from typing import Any, Literal, Optional

from gql import Client
from gql.transport.requests import RequestsHTTPTransport
from graphql import DocumentNode

_PLATFORM_CORE_PUBLIC_GRAPHQL_HOST = (
    "https://public.enterprise-platform-development.com/graphql"
)
_PLATFORM_COMPUTE_PUBLIC_GRAPHQL_HOST = (
    "https://compute.enterprise-platform-development.com/graphql"
)


class ClientBase(Client):
    url: str

    def __init__(self, *, token: str, **kwargs):
        headers = {"authorization": f"compute::user-token::{token}"}
        transport = RequestsHTTPTransport(self.url, headers=headers, timeout=120)
        super().__init__(transport=transport, **kwargs)

    # def execute(
    #     self,
    #     document: DocumentNode,
    #     variable_values: Optional[dict[str, Any]] = ...,
    #     operation_name: Optional[str] = ...,
    #     serialize_variables: Optional[bool] = ...,
    #     parse_result: Optional[bool] = ...,
    #     *,  # https://github.com/python/mypy/issues/7333#issuecomment-788255229
    #     get_execution_result: Literal[False] = ...,
    #     **kwargs,
    # ) -> dict[str, Any]:
    #     result = super().execute(
    #         document,
    #         variable_values=variable_values,
    #         operation_name=operation_name,
    #         serialize_variables=serialize_variables,
    #         parse_result=parse_result,
    #         get_execution_result=get_execution_result,
    #         **kwargs,
    #     )


class ComputeGraphqlClient(ClientBase):
    url = _PLATFORM_COMPUTE_PUBLIC_GRAPHQL_HOST


class PublicGraphqlClient(ClientBase):
    url = _PLATFORM_CORE_PUBLIC_GRAPHQL_HOST
