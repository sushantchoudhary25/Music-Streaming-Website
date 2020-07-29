from music_app import app, crsr
from flask import render_template, request, redirect
from music_app.sql import sql


@app.route("/")
def home():
    return render_template("homepage.html")


def insert_into_playlist(req):
    try:
        crsr.execute(sql.check_for_duplicate.format(req.get("url")))

        res = crsr.fetchall()

        if len(res) == 0:
            query = sql.insert_statement.format(req.get("title"), req.get("artist"),
                                                req.get("album"), req.get("song"), req.get("url"))
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
    if len(playlist) != 0:
        print(playlist)
        records = True
    return render_template("playlist.html", playlist=playlist, records=records)