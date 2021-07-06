from client import get_track
from loudness_wars import add_album_to_database, create_track_album_join
from db import get_db_connection
from concurrent.futures import ThreadPoolExecutor


def backfill_albums_from_tracks():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM track")

    pool = ThreadPoolExecutor()
    for (id,) in cursor.fetchall():
        future = pool.submit(get_track, id)
        track = future.result()
        add_album_to_database(track["album"])
        create_track_album_join(track, track["album"])


if __name__ == "__main__":
    backfill_albums_from_tracks()

