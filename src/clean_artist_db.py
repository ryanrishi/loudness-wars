from client import get_artist, get_track
from loudness_wars import add_artist_to_database
from db import get_db_connection
from spotipy import SpotifyException
import logging
import coloredlogs

coloredlogs.install()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def remove_non_artists():
    logger.info("Removing non-artists from the artist table")
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM artist")

    artists = cursor.fetchall()
    for id, name in artists:
        try:
            get_artist(id)
        except SpotifyException as e:
            if e.http_status == 404:
                logger.info(f"deleting artist (id={id} name={name})")
                cursor.execute("DELETE FROM artist WHERE id = ?", (id,))   # TODO LIMIT 1
                conn.commit()
            else:
                raise


def synchronize_artists_from_tracks():
    logger.info("Synchronizing artists from tracks table")
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM track")
    for id, name in cursor.fetchall():
        track = get_track(id)
        for artist in track["artists"]:
            add_artist_to_database(artist)


def clean_up_track_artist_joins():
    logger.info("Removing invalid track_artist_join records")
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT track.id, taj.artist_id FROM track
            JOIN track_artist_join taj ON taj.track_id = track.id
            LEFT OUTER JOIN artist ON taj.artist_id = artist.id
        WHERE artist.name IS NULL
    """)
    track_artist_joins_with_invalid_artists = cursor.fetchall()
    logger.info(f"Will delete {len(track_artist_joins_with_invalid_artists)} track_artist_joins")
    for track_id, artist_id in track_artist_joins_with_invalid_artists:
        cursor.execute("DELETE FROM track_artist_join WHERE track_id = ? AND artist_id = ?", (track_id, artist_id))
        conn.commit()

if __name__ == "__main__":
    remove_non_artists()
    synchronize_artists_from_tracks()
    clean_up_track_artist_joins()
