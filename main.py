from loudness_wars.client import spotify
import logging
import csv
import json

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
TRACKS_DIR = "out/tracks"


def get_track(track):
    '''
        Parameters:
            - track.title - the title of the track
            - track.artist - the artist of the track
    '''
    results = spotify.search("{} {}".format(track["title"], track["artist"]))
    if results["tracks"] and results["tracks"]["items"]:
        return results["tracks"]["items"][0]     # TODO make sure this gets the correct track


if __name__ == "__main__":
    with open(INFILE, "r") as f:
        input = csv.DictReader(f)
        for song in input:
            track = get_track(song)
            if track:
                logger.info("here")
                logger.info("Found track {} for {} - {}".format(track["id"], song["title"], song["artist"]))
                with open("{}/{}.json".format(TRACKS_DIR, track["id"]), "w") as outfile:
                    outfile.write(json.dumps(track))

    # store track_id
    # (maybe) sanity check / confirm "is this your track?" / add some sort of confidence score

    # for each track, get audio analysis
