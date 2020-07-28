from music_app import app


@app.route("/")
def home():
    return "Home Page"
