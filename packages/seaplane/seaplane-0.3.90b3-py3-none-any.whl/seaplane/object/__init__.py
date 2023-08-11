from typing import List

from ..configuration import config

from ..api.api_object_storage import ObjectStorageAPI

class ObjectStorageWrapper:

    def __init__(self) -> None:                
        pass

    def list(self) -> List[str]:
        api = ObjectStorageAPI(config)
        return api.list()

    def create_bucket(self, name: str) -> str:
        api = ObjectStorageAPI(config)
        return api.create_bucket(name)

    def delete_bucket(self, name: str) -> str:
        api = ObjectStorageAPI(config)
        return api.delete_bucket(name)

    def list_bucket(self, bucket_name: str, path_prefix: str) -> List[str]:
        api = ObjectStorageAPI(config)
        return api.delete_bucket(bucket_name, path_prefix)

    def download(self, bucket_name: str, path: str) -> bytes:        
        api = ObjectStorageAPI(config)
        return api.download(bucket_name, path)
    
    def upload(self, bucket_name: str, path: str, object: bytes) -> str:
        api = ObjectStorageAPI(config)
        return api.upload(bucket_name, path, object)
    
    def upload_file(self, bucket_name: str, path: str, object_path: str) -> str:
        api = ObjectStorageAPI(config)
        return api.upload_file(bucket_name, path, object_path)
    
    def delete(self, bucket_name: str, path: str) -> str:
        api = ObjectStorageAPI(config)
        return api.delete(bucket_name, path)