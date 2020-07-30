create_table = "create table if not exists playlist(title varchar(255), artist varchar(255), " \
               "album varchar(255), url varchar(255) PRIMARY KEY);"

insert_statement = "INSERT INTO playlist VALUES('{}', '{}', '{}', '{}')"

check_for_duplicate = "SELECT * from playlist where url = '{}'"

fetch_songs = "SELECT * FROM playlist"

search = "SELECT * FROM playlist where {} = '{}'"
