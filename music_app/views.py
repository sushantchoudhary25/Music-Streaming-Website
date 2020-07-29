from music_app import app
from flask import render_template


@app.route("/")
def home():
    return render_template("homepage.html")
