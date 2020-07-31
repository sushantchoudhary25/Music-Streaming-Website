from music_app import app, crsr
from flask import render_template, request, redirect
from music_app.sql import sql
import uuid, os
from music_app.storage import Storage


@app.route("/")
def home():
    return render_template("homepage.html")


def get_unique_url(filename):
    return "https://sushant25.blob.core.windows.net/" + app.config.get("STORAGE_CONTAINER_NAME") + "/" + filename


def insert_into_playlist(song_id, title, artist, album, filename):
    try:

        if not check_existing_record(title, artist, album):
            query = sql.insert_statement.format(song_id, title, artist, album, get_unique_url(filename))
            crsr.execute(query)
            app.logger.info("Inserted record successfully")
    except Exception as err:
        raise err


def check_existing_record(title, artist, album):
    try:
        crsr.execute(
            "SELECT * from playlist where artist = '{}' and album = '{}' and title = '{}'".format(artist, album, title))
        res = crsr.fetchall()
        if len(res) == 0:
            return False
        return True
    except Exception as err:
        raise err


def allowed_extenstion(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config.get("ALLOWED_IMAGE_EXTENSIONS"):
        return True
    return False


def allowed_filesize(filesize):
    if int(filesize) <= app.config["MAX_CONTENT_SIZE"]:
        return True
    else:
        return False


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":

        if request.files:
            if "filesize" in request.cookies:
                if not allowed_filesize(request.cookies["filesize"]):
                    app.logger.info("Filesize exceeded maximum limit")
                    return render_template("upload.html", message="please upload filesize less than 10MB")

                req = request.form
                title = req.get("title")
                artist = req.get("artist")
                album = req.get("album")

                if check_existing_record(title, artist, album):
                    return redirect(request.url)

                song = request.files["song"]

                if song.filename == "":
                    app.logger.info("Invalid file name")
                    return render_template("upload.html", message="invalid file name")

                if not allowed_extenstion(song.filename):
                    app.logger.info("invalid Extension")
                    return render_template("upload.html", message="invalid extenstion, please upload mp3")

                song_id = str(uuid.uuid4())

                unique_filename = song_id + ".mp3"
                path = os.path.join(app.config.get("PROJECT_ROOT_DIR") + app.config.get("UPLOAD_FILE_PATH"),
                                    unique_filename)

                song.save(path)

                Storage.upload_file(path, unique_filename)

                insert_into_playlist(song_id, title, artist, album, unique_filename)

                os.remove(path=path)
                return redirect(request.url)

    return render_template("upload.html")


def fetch_all_songs():
    try:
        crsr.execute(sql.fetch_songs)
        return crsr.fetchall()
    except Exception as err:
        raise err


@app.route("/playlist")
def view_playlist():
    playlist = fetch_all_songs()
    records = False
    if playlist:
        records = True
    return render_template("playlist.html", playlist=playlist, records=records)


def search_songs(category, value):
    try:
        crsr.execute(sql.search.format(category, value))
        return crsr.fetchall()
    except Exception as err:
        raise err


@app.route("/search-database", methods=["POST"])
def search_database():
    req = request.form

    category = str(req.get("category")).lower()
    value = req.get("search")

    if category not in ["artist", "album", "title"]:
        return render_template("search.html", message="category should be [Artist, Title, Album]")

    playlist = search_songs(category=category, value=value)

    if not playlist:
        return render_template("search.html", message="No Record Found")

    return render_template("playlist.html", playlist=playlist, records=True)


@app.route("/search")
def search():
    return render_template("search.html", message=None)


def delete_record(song_id):
    try:
        crsr.execute(sql.delete.format(song_id))
    except Exception as err:
        raise err


@app.route("/delete/<song_id>", methods=["GET", "POST"])
def delete(song_id):
    delete_record(song_id)
    Storage.delete_file
    playlist = fetch_all_songs()
    if not playlist:
        return render_template("playlist.html", playlist=playlist, records=False)

    return render_template("playlist.html", playlist=playlist, records=True)


def get_url(song_id):
    try:
        crsr.execute("SELECT title, url from playlist where songId = '{}'".format(song_id))
        return crsr.fetchall()[0]
    except Exception as err:
        raise err


@app.route("/play/<song_id>")
def play(song_id):
    link = get_url(song_id)
    return render_template("player.html", link=link[1], title=link[1])
