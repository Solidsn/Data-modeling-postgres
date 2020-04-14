# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
songplay_id SERIAL PRIMARY KEY,
start_time  bigint,
user_id int,
level TEXT,
song_id TEXT ,
artist_id TEXT ,
session_id int,
location TEXT,
user_agent TEXT,
FOREIGN KEY (user_id) REFERENCES users(user_id),
FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
FOREIGN KEY (song_id) REFERENCES songs(song_id),
FOREIGN KEY (start_time) REFERENCES time(start_id))""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
user_id int PRIMARY KEY,
firstName TEXT,
lastName TEXT,
gender character(1),
level character(4)
)""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
song_id TEXT PRIMARY KEY,
title TEXT,
artist_id TEXT,
year INT,
duration FLOAT)""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
artist_id TEXT PRIMARY KEY,
name TEXT,
location TEXT,
latitude FLOAT,
longitude FLOAT)""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
start_id bigint PRIMARY KEY,
hour int,
day int,
week int,
month int,
year int,
weekday int)""")

# INSERT RECORDS
songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)""")

user_table_insert = ("""
INSERT INTO users (user_id, firstName,lastName, gender, level) VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (user_id) DO UPDATE
SET level = EXCLUDED.level;""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (song_id) DO NOTHING;""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (artist_id) DO UPDATE 
SET location = EXCLUDED.location, latitude = EXCLUDED.latitude, longitude = EXCLUDED.longitude;""")


time_table_insert = ("""
INSERT INTO time (start_id, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_id) DO NOTHING""")

# FIND SONGS

song_select = (""" 
SELECT songs.song_id, artists.artist_id
FROM songs INNER JOIN artists ON (songs.artist_id = artists.artist_id)
WHERE songs.title = %s and artists.name = %s and songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [artist_table_create, song_table_create, user_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]