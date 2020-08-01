from music_app import app


class Helper(object):
    @staticmethod
    def get_unique_url(filename):
        return app.config.get("BLOB_URL") + filename

    @staticmethod
    def allowed_extenstion(filename):
        if not "." in filename:
            return False

        ext = filename.rsplit(".", 1)[1]

        if ext.upper() in app.config.get("ALLOWED_IMAGE_EXTENSIONS"):
            return True
        return False

    @staticmethod
    def allowed_filesize(filesize):
        if int(filesize) <= app.config["MAX_CONTENT_SIZE"]:
            return True
        else:
            return False
