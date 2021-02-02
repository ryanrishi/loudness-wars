from client import search_for_track
from fuzzywuzzy import fuzz
import logging
from glob import glob
from os import path
import csv
from csv import DictReader
import sqlite3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#   for each billboard chart
#       read chart csv
#       search for track (song + artist)
#       filter results for best match
#           - artist name
#           - release year
#           - song name
#       save spotify track id

#   for each track
#       get analysis for spotify track id
#       save analysis




# def get_loudness_for_track(track_id):
#     results = get_track_analysis(track_id)
#     return results["loudness"]
#
#
# def find_track_in_results(results, name, artist):
#     """
#         iterate over tracks, fuzzy matching on track title and artist
#         choose track with highest ratio for name/artist
#         TOOD consider weighting by release date, in case there are rereleases/remasters
#     """
#     found = None
#     found_name_ratio = 0
#     found_artist_ratio = 0
#     for track in results["tracks"]["items"]:
#         name_ratio = fuzz.ratio(track["name"], name)
#         for found_artist in track["artists"]:
#             artist_ratio = fuzz.ratio(found_artist["name"], artist)
#             if (artist_ratio > found_artist_ratio) and (name_ratio > found_name_ratio):
#                 found = track
#                 found_name_ratio = name_ratio
#                 found_artist_ratio = artist_ratio
#     return found

def _get_db_connection():
    try:
        conn = sqlite3.connect(path.join(path.dirname(__file__), "db/spotify.db"))
        return conn
    except Exception as e:
        logger.error(f"Error creating database connection: {e}")


def add_track_to_database(track):
    conn = _get_db_connection()
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
    conn = _get_db_connection()
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
    conn = _get_db_connection()
    cursor = conn.cursor()

    for artist in track["artists"]:
        try:
            cursor.execute("INSERT INTO track_artist_join (track_id, artist_id) VALUES (?, ?)", (track["id"], artist["id"]))
            conn.commit()
            logger.info(f"Created track_artist_join records for {track['name']} - {artist['name']}")
        except sqlite3.IntegrityError:
            # this will happen if we re-run the application from the beginning
            logger.debug(f"Failed to create track_artist_join records for {track['name']} - {artist['name']}")


if __name__ == "__main__":
    unfound_tracks = []

    for year in range(2020, 2020 + 1):
        with open(f"{path.dirname(path.dirname(__file__))}/billboard/{year}.csv", "r") as f:
            reader = DictReader(f)
            for row in reader:
                track = search_for_track(row['song'], row['artist'], year)
                if track:
                    for artist in track["artists"]:
                        add_artist_to_database(artist)
                    add_track_to_database(track)
                    create_track_artist_joins(track)
                else:
                    unfound_tracks.append((row['song'], row['artist'], year))

    if unfound_tracks:
        logger.warning(f"Could not find {len(unfound_tracks)} tracks")
        unfound_tracks_file = path.join(path.dirname(path.dirname(__file__)), "out/not-found.csv")
        with open(unfound_tracks_file, "w") as f:
            writer = csv.writer(f)
            writer.writerow(['song', 'artist', 'year'])

            for track in unfound_tracks:
                writer.writerow(track)

        logger.info(f"Wrote unfound tracks to {unfound_tracks_file}")


    # for year, tracks in billboard_by_year.iteritems():
    #     logger.info("=== Starting year %s ===" % year)
    #     for track in tracks:
    #         rank = track['Position']
    #         artist = track['Artist']
    #         song = track['Song Title']
    #         logger.debug("Getting track info for %s by %s" % (song, artist))
    #         results = get_track_info(song, artist)
    #         found = find_track_in_results(results, song, artist)
    #         if not found:
    #             logger.warn("Could not find track %s by %s" % (song, artist))
    #         else:
    #             logger.debug("Searched for %s - %s" % (song, artist))
    #             logger.debug("Found %s - %s" % (found["name"], ' / '.join([a["name"] for a in found["artists"]])))
    #             loudness = get_loudness_for_track(found["id"])
    #             logger.debug("Loudness: %d" % loudness)
    #             track["Loudness"] = loudness
    #             track["id"] = found["id"]
    #
    #     filename = "%s-results.csv" % year
    #     write_results_to_file(filename, tracks)
