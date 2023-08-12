import gzip
import http.client
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional
from uuid import uuid4

_TEMPORARY_STORAGE_PATH = os.environ.get("TEMPORARY_STORAGE_PATH", "/tmp")
_PLATFORM_CORE_API_HOST = os.environ.get(
    "PLATFORM_CORE_API_HOST",
    "https://api.enterprise-platform-development.com",
)


class File:
    _id: str
    _path: str
    _name: str

    def __init__(self, path: str, *, name: Optional[str] = None):
        self._id = str(uuid4())
        self._path = path
        self._name = name or path

    def __str__(self) -> str:
        return self.path

    @property
    def path(self) -> str:
        return self._download()

    @staticmethod
    def _get_authentication_header(api_key: Optional[str]):
        machine_token = os.environ.get("MACHINE_TOKEN")
        if machine_token is not None:
            return f"compute::machine::{machine_token}"

        if api_key is not None:
            return f"compute::user-token::{api_key}"

        raise ValueError(
            "No access token found in the environment. "
            "Is this a valid platform compute runtime?"
        )

    def _execute(self, path: str, data: dict, *, api_key: Optional[str] = None):
        url = f"{_PLATFORM_CORE_API_HOST}/{path}"
        headers = {
            "content-type": "application/json",
            "accept": "application/json",
            "authorization": self._get_authentication_header(api_key),
        }

        data_to_send = json.dumps({**data, "tenant_id": "compute"}).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=data_to_send,
            headers=headers,
            method="POST",
        )

        with urllib.request.urlopen(request) as response:
            if response.status != 200:
                raise urllib.error.HTTPError(
                    url,
                    response.status,
                    response.reason,
                    response.headers,
                    None,
                )
            response_data = response.read()
            return json.loads(response_data.decode("utf-8"))

    def _download(self, *, api_key: Optional[str] = None):
        """
        Get the file from the objects service and download it
        to a temporary location on the local filesystem. In the
        future, the environment can inject a custom storage class
        that can access the file.
        """
        object_data = self._execute(
            "objects/get_object",
            {"object_id": self._id},
            api_key=api_key,
        )
        with urllib.request.urlopen(object_data["get_url"]) as response:
            object_bytes = response.read()
            object_path = os.path.join(_TEMPORARY_STORAGE_PATH, self._path)
            with open(object_path, "wb") as file:
                file.write(gzip.decompress(object_bytes))
                return object_path

    def download(self, *, api_key: str):
        self._download(api_key=api_key)

    def _upload(self, data: bytes, *, api_key: Optional[str] = None):
        object_ = self._execute(
            "objects/get_object_for_upload",
            data={"object_id": self._id, "object_type": "DOCUMENT"},
            api_key=api_key,
        )

        boundary = f"------------------------{uuid4()}"
        body = []

        post_url = object_["post_data"]["url"]
        post_fields = object_["post_data"]["fields"]

        for key, value in post_fields.items():
            body.append(f"--{boundary}")
            body.append(f'Content-Disposition: form-data; name="{key}"')
            body.append("")
            body.append(value.encode("utf-8"))

        # Add the file to be uploaded
        body.append(f"--{boundary}")
        body.append(
            'Content-Disposition: form-data; name="file"; filename="your_filename.ext"'
        )
        body.append("Content-Type: application/octet-stream")
        body.append("")
        body.append(gzip.compress(data))

        # End the request body with the boundary
        body.append(f"--{boundary}--")
        body.append("")

        # Join all the parts of the body into a single string
        body = [
            part.encode("utf-8") if isinstance(part, str) else part for part in body
        ]
        body = b"\r\n".join(body)

        parsed_url = urllib.parse.urlsplit(post_url)
        headers = {
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Content-Length": str(len(body)),
        }

        connection = http.client.HTTPSConnection(parsed_url.netloc)
        try:
            connection.request("POST", parsed_url.path, body, headers)
            response = connection.getresponse()
            response_data = response.read().decode()

            if response.status == 204 or response.status == 200:
                print(f"{self._name} uploaded successfully.")
            else:
                print(f"Upload failed with status {response.status}: {response_data}")
        finally:
            connection.close()

    def upload(self, *, api_key: str):
        with open(self._path, "rb") as file:
            data = file.read()
            self._upload(data, api_key=api_key)
