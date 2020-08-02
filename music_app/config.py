import os


class Config(object):
    """
    This class will hold the basic configuration variables
    """

    DEBUG = True
    STORAGE_ACCOUNT_CONNECTION_STRING = os.getenv("STORAGE_ACCOUNT_CONNECTION_STRING")
    PROJECT_ROOT_DIR = os.getenv("PROJECT_ROOT_DIR")
    STORAGE_CONTAINER_NAME = os.getenv("STORAGE_CONTAINER_NAME")
    UPLOAD_FILE_PATH = "/music_app/uploads/"
    BLOB_URL = os.getenv("BLOB_URL")
    ALLOWED_FILE_EXTENSIONS = "MP3"
    MAX_CONTENT_SIZE = 5 * 1024 * 1024
