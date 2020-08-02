from music_app import app, connection, storage_client
from flask import render_template, request, redirect
import uuid, os
from music_app.helpers import Helper


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":

        if request.files:
            if "filesize" in request.cookies:
                if not Helper.allowed_filesize(request.cookies["filesize"]):
                    app.logger.info("Filesize exceeded maximum limit")
                    return render_template("upload.html", message="please upload filesize less than {}MB".
                                           format(app.config.get("MAX_CONTENT_SIZE") // (1024 * 1024)))

                req = request.form
                title = req.get("title")
                artist = req.get("artist")
                album = req.get("album")

                if connection.check_existing_record(title, artist, album):
                    return redirect(request.url)

                song = request.files["song"]

                if song.filename == "":
                    app.logger.info("Invalid file name")
                    return render_template("upload.html", message="invalid file name")

                if not Helper.allowed_extenstion(song.filename):
                    app.logger.info("invalid Extension")
                    return render_template("upload.html", message="invalid extenstion, please upload mp3")

                song_id = str(uuid.uuid4())

                unique_filename = song_id + ".mp3"
                path = os.path.join(app.config.get("PROJECT_ROOT_DIR") + app.config.get("UPLOAD_FILE_PATH"),
                                    unique_filename)

                song.save(path)

                storage_client.upload_file(path, unique_filename)

                connection.insert_into_playlist(song_id, title, artist, album, unique_filename)

                os.remove(path=path)
                return render_template("upload.html", message="song uploaded successfully")

    return render_template("upload.html")


@app.route("/playlist")
def view_playlist():
    playlist = connection.fetch_all_songs()
    records = False
    if playlist:
        records = True
    return render_template("playlist.html", playlist=playlist, records=records)


@app.route("/search-database", methods=["POST"])
def search_database():
    req = request.form

    category = str(req.get("category")).lower()
    value = req.get("search")

    if category not in ["artist", "album", "title"]:
        return render_template("search.html", message="category should be [Artist, Title, Album]")

    playlist = connection.search_songs(category=category, value=value)

    if not playlist:
        return render_template("search.html", message="No Record Found")

    return render_template("playlist.html", playlist=playlist, records=True)


@app.route("/search")
def search():
    return render_template("search.html", message=None)


@app.route("/delete/<song_id>", methods=["GET", "POST"])
def delete(song_id):
    connection.delete_record(song_id)
    storage_client.delete_blob(song_id)
    playlist = connection.fetch_all_songs()
    if not playlist:
        return render_template("playlist.html", playlist=playlist, records=False)

    return render_template("playlist.html", playlist=playlist, records=True)


@app.route("/play/<song_id>")
def play(song_id):
    link = connection.get_url(song_id)
    return render_template("player.html", link=link[1], title=link[1])


@app.route("/stream")
def stream():
    return redirect("/playlist")