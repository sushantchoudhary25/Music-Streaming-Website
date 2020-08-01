from flask import Flask

app = Flask(__name__)
app.config.from_object("music_app.config.Config")

from music_app.storage import Storage
from music_app.sql.sql import SQL

connection = SQL()
connection.cursor.execute(connection.create_table)

storage_client = Storage()
from music_app import views
from music_app import config
