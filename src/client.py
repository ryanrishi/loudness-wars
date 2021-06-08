from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from config import config
import logging
import inquirer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

CLIENT_ID = config.get("spotify", "CLIENT_ID")
CLIENT_SECRET = config.get("spotify", "CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_primary_artist_name(artist_name):
    features = ("Featuring", "With", "x", "X", "&")
    primary_artist = artist_name
    for feature in features:
        if feature in primary_artist:
            primary_artist = artist_name.split(feature)[0].strip()

    if primary_artist != artist_name:
        logger.info(f"Extracted {primary_artist} as primary artist name for {artist_name}")

    return primary_artist


def search_for_track(track_name, artist_name: str, year):
    # TODO be smarter about this - use featured artist to match if multiple artists returned from Spotify
    artist_name = get_primary_artist_name(artist_name)

    query = f"{track_name} {artist_name}"
    results = sp.search(query)
    if results["tracks"] and results["tracks"]["items"]:
        for track in results["tracks"]["items"]:
            # TODO better matching on things like "Life Is Good (feat. Drake)", when query is "Life Is Good"
            # TODO Señorita → Senorita - or just clean up input file to have ñ
            if track["name"].lower() == track_name.lower() or track_name.lower() in track["name"].lower():
                for artist in track["artists"]:
                    if artist["name"].lower() == artist_name.lower():
                        logger.info(f"For {track_name} by {artist_name}, found {track['name']} by {track['artists'][0]['name']}")
                        return track

        # prompt to choose a track
        choices_dict = {}
        for track in results["tracks"]["items"]:
            message = f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])} ({track['album']['release_date']})"
            choices_dict[message] = track["id"]
        # choices = [f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])} ({track['album']['release_date']})" for track in results["tracks"]["items"]]
        questions = [
            inquirer.List("track", message=f"Which track best matches {track_name} by {artist_name} ({year})?", choices=choices_dict.keys())
        ]
        chosen = inquirer.prompt(questions)
        # logger.info(f"chosen:\t{chosen}")
        # logger.info(f"choices_dict:\t{choices_dict}")
        chosen_track_id = choices_dict[chosen["track"]]
        return list(track for track in results["tracks"]["items"] if track["id"] == chosen_track_id)[0]
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
