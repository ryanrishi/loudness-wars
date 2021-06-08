from client import search_for_track
import logging
import sqlite3
from db import get_db_connection
from billboard import mark_track_as_found, find_billboard_chart_track, find_tracks_by_year

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def add_track_to_database(track):
    conn = get_db_connection()
    cursor = conn.cursor()

    # check if track already exists in database
    cursor.execute("SELECT * FROM track where id = ?", (track["id"],))

    if not cursor.fetchall():
        # add track to database
        cursor.execute("INSERT INTO TRACK (id, name) VALUES (?, ?)", (track["id"], track["name"]))
        conn.commit()
        logger.info(f"Added track to database: {track['id']} ({track['name']})")
    else:
        logger.debug(f"Track already exists in database; skipping: {track['id']} ({track['name']})")


def add_artist_to_database(artist):
    conn = get_db_connection()
    cursor = conn.cursor()

    # check if artist already exists in database
    cursor.execute("SELECT * FROM artist WHERE id = ?", (artist["id"],))

    if not cursor.fetchall():
        # add artist to database
        cursor.execute("INSERT INTO artist (id, name) VALUES (?, ?)", (artist["id"], artist["name"]))
        conn.commit()
        logger.info(f"Added artist to database: {artist['id']} ({artist['name']})")
    else:
        logger.debug(f"Artist already exists in database; skipping: {artist['id']} ({artist['name']})")


def create_track_artist_joins(track):
    conn = get_db_connection()
    cursor = conn.cursor()

    for artist in track["artists"]:
        try:
            cursor.execute("INSERT INTO track_artist_join (track_id, artist_id) VALUES (?, ?)", (track["id"], artist["id"]))
            conn.commit()
            logger.info(f"Created track_artist_join records for {track['name']} - {artist['name']}")
        except sqlite3.IntegrityError:
            # this will happen if we re-run the application from the beginning
            logger.debug(f"Failed to create track_artist_join records for {track['name']} - {artist['name']}")


def find_track(track_name, artist_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM track
            INNER JOIN track_artist_join taj on track.id = taj.track_id
            INNER JOIN artist on artist.id = taj.artist_id
        WHERE TRUE
            AND track.name = ?
            AND artist.name = ?
    ''', (track_name, artist_name))

    found_track = cursor.fetchone()
    if not found_track:
        logger.info(f"Track not found: {track_name} by {artist_name}")

    return found_track


if __name__ == "__main__":
    for track in find_tracks_by_year(2020, 2020 + 1):
        if track["found"]:
            logger.debug(f"Track is already marked as found; not reprocessing: {track['song']} by {track['artist']} ({track['year']})")
            continue

        spotify_track = search_for_track(track["song"], track["artist"], track["year"])
        if spotify_track:
            for artist in spotify_track["artists"]:
                add_artist_to_database(spotify_track)
            add_track_to_database(spotify_track)
            create_track_artist_joins(spotify_track)
            mark_track_as_found(track['id'])