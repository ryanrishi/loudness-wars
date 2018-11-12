from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from config import config


CLIENT_ID = config.get("spotify", "CLIENT_ID")
CLIENT_SECRET = config.get("spotify", "CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


if __name__ == "__main__":
    print sp.search('Radiohead')
