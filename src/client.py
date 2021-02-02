from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from config import config
import logging
from datetime import datetime
from types import SimpleNamespace

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

CLIENT_ID = config.get("spotify", "CLIENT_ID")
CLIENT_SECRET = config.get("spotify", "CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def search_for_track(track_name, artist_name, year):
    query = f"{track_name} {artist_name}"
    results = sp.search(query)
    if results["tracks"]:
        for track in results["tracks"]["items"]:
            if track["name"] == track_name:
                for artist in track["artists"]:
                    if artist["name"] == artist_name:
                        logger.info(f"For {track_name} by {artist_name}, found {track}")
                        return track
                logger.warning(f"No artist match found for {track_name}")
        logger.warning(f"No match found for {track_name} by {artist_name}")
    else:
        logger.warning(f"Found no tracks for {track_name} by {artist_name}")

        # else
        # fuzzy match on track name + artist name?
        # filter by release date closest to and prior to year?

def get_track_info(name, artist):
    query = '%s %s' % (name, artist)
    return sp.search(q=query)


def get_track_analysis(track_id):
    return sp.audio_analysis(track_id)


if __name__ == "__main__":
    results = sp.search('Creep Radiohead')
    logger.info(results['tracks']['items'])
