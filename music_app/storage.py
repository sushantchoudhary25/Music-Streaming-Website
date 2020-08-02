from music_app import app
from azure.storage.blob import BlobServiceClient


class Storage(object):
    """
    Storage class will be used to upload and delete the data from blob storage
    """

    def __init__(self):
        self.connection_string = app.config.get("STORAGE_ACCOUNT_CONNECTION_STRING")

    def get_blob_client(self, file_name):
        """
        This will return the blob client for the file

        :param file_name: the name with which file will be stored on blob storage
        :return:
        """

        try:
            service_client = BlobServiceClient.from_connection_string(self.connection_string)
            blob_client = service_client.get_blob_client(container=app.config.get("STORAGE_CONTAINER_NAME"), blob=file_name)
            return blob_client
        except Exception as err:
            raise err

    def upload_file(self, file_path, file_name):
        """
        This function will upload the local file to blob storage with provided name

        :param file_path: path of file on local file system
        :param file_name: the name with which file will be stored on blob storage
        :return:
        """

        try:
            blob_client = self.get_blob_client(file_name=file_name)

            with open(file_path, "rb") as blob:
                blob_client.upload_blob(blob)
        except Exception as err:
            raise err

    def delete_blob(self, blob_id):
        """
        This function will delete the file from blob storage

        :param blob_id: blob id of the file stored on blob storage
        :return:
        """

        try:
            file_name = blob_id + ".mp3"
            blob_client = self.get_blob_client(file_name=file_name)
            blob_client.delete_blob()
        except Exception as err:
            raise err
