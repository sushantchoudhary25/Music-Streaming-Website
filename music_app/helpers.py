from music_app import app


class Helper(object):
    """
    Helper class will contain helper functions used by different router functions
    """

    @staticmethod
    def get_unique_url(filename):
        """
        This will return the url for the file

        :param filename: name of the local file
        :return: returns the url
        """

        return app.config.get("BLOB_URL") + filename

    @staticmethod
    def allowed_extenstion(filename):
        """
        This function will check the valid file extension uploaded by users

        :param filename: name of the file uploaded by user
        :return: true if file extension is allowed else false
        """

        # if file name is not valid
        if not "." in filename:
            return False

        ext = filename.rsplit(".", 1)[1]

        # check for valid extension from list of valid extensions
        if ext.upper() in app.config.get("ALLOWED_FILE_EXTENSIONS"):
            return True
        return False

    @staticmethod
    def allowed_filesize(filesize):
        """
        check for valid file size of uploaded file

        :param filesize: size of uploaded file
        :return: true if file size is under acceptable size else false
        """

        if int(filesize) <= app.config["MAX_CONTENT_SIZE"]:
            return True
        else:
            return False
