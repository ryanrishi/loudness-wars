from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from config import config


CLIENT_ID = config.get("spotify", "CLIENT_ID")
CLIENT_SECRET = config.get("spotify", "CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_track_info(name, artist):
    query = '%s %s' % (name, artist)
    results = sp.search(q=query)
    return results


def get_track_analysis(track_id):
    results = sp.audio_analysis(track_id)
    return results["track"]


if __name__ == "__main__":
    results = sp.search('Creep Radiohead')
    import pprint
    print pprint.pprint(results['tracks']['items'])
