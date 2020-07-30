from music_app import app, crsr
from flask import render_template, request, redirect
from music_app.sql import sql
import uuid


@app.route("/")
def home():
    return render_template("homepage.html")


def insert_into_playlist(req):
    try:
        crsr.execute(sql.check_for_duplicate.format(req.get("url")))

        res = crsr.fetchall()

        if len(res) == 0:
            query = sql.insert_statement.format(uuid.uuid4(), req.get("title"), req.get("artist"),
                                                req.get("album"), req.get("url"))
            crsr.execute(query)
            app.logger.info("Inserted record successfully")
    except Exception as err:
        raise err


@app.route("/upload", methods=["GET", "POST"])
def upload_song():
    if request.method == "POST":
        insert_into_playlist(request.form)
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
    playlist = fetch_all_songs()
    if not playlist:
        return render_template("playlist.html", playlist=playlist, records=False)

    return render_template("playlist.html", playlist=playlist, records=True)