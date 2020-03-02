from loudness_wars.client import spotify
import logging
import coloredlogs
import csv
import json
from fuzzywuzzy import fuzz

coloredlogs.install()
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

"""
TODO
- don't search for songs that have already been found
"""


INFILE = "in.csv"
"""
    out/
    |- tracks/
       |- 12345.json
       |- 67890.json
"""
OUT_DIR = "out"
TRACKS_DIR = "{}/tracks".format(OUT_DIR)
FOUND_FILE = "{}/found".format(OUT_DIR)


def find_track(song):
    '''
        Parameters:
            - song.title - the title of the track
            - song.artist - the artist of the track
    '''
    results = spotify.search("{} {}".format(song["title"], song["artist"]))

    found = None
    found_name_ratio = 0
    found_artist_ratio = 0

    for track in results["tracks"]["items"]:
        name_ratio = fuzz.ratio(track["name"], song["title"])
        for artist in track["artists"]:
            artist_ratio = fuzz.ratio(artist["name"], song["artist"])
            if artist_ratio > found_artist_ratio and name_ratio > found_name_ratio:
                found = track
                found_name_ratio = name_ratio
                found_artist_ratio = artist_ratio

    return found


if __name__ == "__main__":
    found_tracks = 0
    with open(INFILE, "r") as f:
        input = csv.DictReader(f)
        for song in input:
            # check if we've already found the track (based on title and artist name)
            track_key = "{} - {}".format(song["title"], song["artist"])
            with open(FOUND_FILE, "r") as f:
                if track_key in f.read():
                    logger.debug("{} already found".format(track_key))
                    continue

            track = find_track(song)
            if track:
                logger.debug("Found track {} for {}".format(track["id"], track_key))
                with open("{}/{}.json".format(TRACKS_DIR, track["id"]), "w") as outfile:
                    outfile.write(json.dumps(track))

                # mark as found
                with open(FOUND_FILE, "a") as f:
                    f.write("{}\n".format(track_key))
            else:
                logger.warning("Could not find track for {}".format(track_key))

    logger.info("Getting analysis for tracks")

    # store track_id
    # (maybe) sanity check / confirm "is this your track?" / add some sort of confidence score

    # for each track, get audio analysis
