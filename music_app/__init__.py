from flask import Flask

app = Flask(__name__)
app.config.from_object("music_app.config.Config")

from music_app import views
from music_app import config
