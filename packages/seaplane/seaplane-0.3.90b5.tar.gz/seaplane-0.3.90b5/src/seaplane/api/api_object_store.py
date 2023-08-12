from typing import Any, Dict, List

import requests

from ..configuration import Configuration, config
from ..util import unwrap
from .api_http import headers
from .api_request import provision_req


class ObjectStorageAPI:
    """
    Class for handle Object Storage API calls.
    """

    def __init__(self, configuration: Configuration = config) -> None:
        self.url = f"{configuration.carrier_endpoint}/object"
        self.req = provision_req(configuration._token_api)

    def list(self) -> List[str]:

        return unwrap(
            self.req(lambda access_token: requests.get(self.url, headers=headers(access_token)))
        )

    def create_bucket(self, name: str) -> Any:
        url = f"{self.url}/{name}"

        return unwrap(
            self.req(lambda access_token: requests.put(url, headers=headers(access_token)))
        )

    def delete_bucket(self, name: str) -> Any:
        url = f"{self.url}/{name}"

        return unwrap(
            self.req(lambda access_token: requests.delete(url, headers=headers(access_token)))
        )

    def list_bucket(self, bucket_name: str, path_prefix: str) -> List[str]:
        url = f"{self.url}/{bucket_name}/list"

        params: Dict[str, Any] = {}
        params["path"] = path_prefix

        return unwrap(
            self.req(
                lambda access_token: requests.get(
                    url, params=params, headers=headers(access_token)
                )
            ).map(lambda objects: [object["name"] for object in objects])
        )

    def download(self, bucket_name: str, path: str) -> bytes:
        url = f"{self.url}/{bucket_name}/store"

        params: Dict[str, Any] = {}
        params["path"] = path

        return unwrap(
            self.req(
                lambda access_token: requests.get(
                    url, params=params, headers=headers(access_token, "application/octet-stream")
                )
            ).map(lambda object: bytes(object))
        )

    def upload(self, bucket_name: str, path: str, object: bytes) -> Any:
        url = f"{self.url}/{bucket_name}/store"

        params: Dict[str, Any] = {}
        params["path"] = path

        return unwrap(
            self.req(
                lambda access_token: requests.put(
                    url,
                    params=params,
                    data=object,
                    headers=headers(access_token, "application/octet-stream"),
                )
            )
        )

    def upload_file(self, bucket_name: str, path: str, object_path: str) -> Any:
        url = f"{self.url}/{bucket_name}/store"

        params: Dict[str, Any] = {}
        params["path"] = path

        with open(object_path, "rb") as file:
            file_data = file.read()

        return unwrap(
            self.req(
                lambda access_token: requests.put(
                    url,
                    params=params,
                    data=file_data,
                    headers=headers(access_token, "application/octet-stream"),
                )
            )
        )

    def delete(self, bucket_name: str, path: str) -> Any:
        url = f"{self.url}/{bucket_name}/store"

        params: Dict[str, Any] = {}
        params["path"] = path

        return unwrap(
            self.req(
                lambda access_token: requests.delete(
                    url, params=params, headers=headers(access_token)
                )
            )
        )
