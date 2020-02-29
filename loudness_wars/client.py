import spotipy
import configparser
from spotipy.oauth2 import SpotifyClientCredentials

config = configparser.ConfigParser()
config.read('config')

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=config.get('spotify', 'client_id'),
        client_secret=config.get('spotify', 'client_secret')
    )
)

if __name__ == "__main":
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])
