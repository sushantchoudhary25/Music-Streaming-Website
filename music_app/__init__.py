from flask import Flask
import sqlite3
from music_app.sql import sql

app = Flask(__name__)
app.config.from_object("music_app.config.Config")

connection = sqlite3.connect(app.config["PROJECT_ROOT_DIR"] + "/Music-Streaming-Website/music_app/data/songs.db", check_same_thread=False)
crsr = connection.cursor()
crsr.execute(sql.create_table)

from music_app import views
from music_app import config
