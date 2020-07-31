import os
from music_app import app
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


class Storage(object):
    connection_string = os.getenv("STORAGE_ACCOUNT_CONNECTION_STRING")

    @staticmethod
    def get_blob_client(file_name):

            service_client = BlobServiceClient.from_connection_string(Storage.connection_string)
            blob_client = service_client.get_blob_client(container=app.config.get("STORAGE_CONTAINER_NAME"), blob=file_name)
            return blob_client

    @staticmethod
    def upload_file(file_path, file_name):
        blob_client = Storage.get_blob_client(file_name=file_name)

        with open(file_path, "rb") as blob:
            blob_client.upload_blob(blob)


if __name__ == '__main__':
    Storage.upload_file("/Users/schoudhary/Music-Streaming-Website/music_app/uploads/sample.txt", "sample.txt")
