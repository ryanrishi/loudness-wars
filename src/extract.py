"""
Extract meaningful information once all of the analysis has been downloaded
"""
from csv import writer
from db import get_db_connection
import logging
import coloredlogs

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
coloredlogs.install()


def generate_csv():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT track.id, track.name track_name, group_concat(artist.name, ', ') artist, album.name album, album.release_date, album.release_date_precision, json_extract(aa.analysis, '$.track.loudness') loudness FROM TRACK
        JOIN track_artist_join ON track_artist_join.track_id = track.id
        JOIN artist ON track_artist_join.artist_id = artist.id
        JOIN track_album_join ON track_album_join.track_id = track.id
        JOIN album ON track_album_join.album_id = album.id
        JOIN audio_analysis aa ON aa.track_id = track.id
        WHERE TRUE
            AND track.name NOT LIKE '%deluxe%'
            AND album.name NOT LIKE '%deluxe%'
        GROUP BY track.id
    ''')

    tracks = cursor.fetchall()
    logger.info(f"Fetched {len(tracks)} tracks")
    with open('out.csv', 'w') as f:
        csv = writer(f)
        headers = ["track_id", "track_name", "artist_name", "album_name", "release_date", "release_date_precision", "loudness"]
        csv.writerow(headers)
        for track in tracks:
            csv.writerow(track)


if __name__ == "__main__":
    generate_csv()
