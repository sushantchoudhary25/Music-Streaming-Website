import sqlite3
from music_app import app
from music_app.helpers import Helper


class SQL(object):
    def __init__(self):
        self.create_table = "create table if not exists playlist(songId varchar(255), title varchar(255), " \
                            "artist varchar(255), album varchar(255), url varchar(255) PRIMARY KEY); "

        self.insert = "INSERT INTO playlist VALUES('{}', '{}', '{}', '{}', '{}')"

        self.fetch = "SELECT * FROM playlist"

        self.search = "SELECT * FROM playlist where {} = '{}'"

        self.delete = "DELETE FROM playlist where songId = '{}'"

        self.duplicate = "SELECT * from playlist where artist = '{}' and album = '{}' and title = '{}'"

        self.url = "SELECT title, url from playlist where songId = '{}'"

        self.connection = sqlite3.connect(app.config["PROJECT_ROOT_DIR"] + "/Music-Streaming-Website/music_app/data"
                                                                           "/songs.db", check_same_thread=False)

        self.cursor = self._get_cursor()

    def _get_cursor(self):
        return self.connection.cursor()

    def check_existing_record(self, title, artist, album):
        try:
            self.cursor.execute(self.duplicate.format(artist, album, title))
            res = self.cursor.fetchall()
            if len(res) == 0:
                return False
            return True
        except Exception as err:
            raise err

    def insert_into_playlist(self, song_id, title, artist, album, filename):
        try:
            if not self.check_existing_record(title, artist, album):
                query = self.insert.format(song_id, title, artist, album, Helper.get_unique_url(filename))
                self.cursor.execute(query)
                app.logger.info("Inserted record successfully")
        except Exception as err:
            raise err

    def fetch_all_songs(self):
        try:
            self.cursor.execute(self.fetch)
            return self.cursor.fetchall()
        except Exception as err:
            raise err

    def search_songs(self, category, value):
        try:
            self.cursor.execute(self.search.format(category, value))
            return self.cursor.fetchall()
        except Exception as err:
            raise err

    def delete_record(self, song_id):
        try:
            self.cursor.execute(self.delete.format(song_id))
        except Exception as err:
            raise err

    def get_url(self, song_id):
        try:
            self.cursor.execute(self.url.format(song_id))
            return self.cursor.fetchall()[0]
        except Exception as err:
            raise err
