from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from config import config
import logging
import inquirer
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

CLIENT_ID = config.get("spotify", "CLIENT_ID")
CLIENT_SECRET = config.get("spotify", "CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_primary_artist_name(artist_name):
    # TODO this is not working for groups like "Earth, Wind, & Fire", "Kool & The Gang"
    features = ("Featuring", "With", "x", "X", "&")
    primary_artist = artist_name
    for feature in features:
        if f" {feature} " in primary_artist:
            primary_artist = artist_name.split(feature)[0].strip()

    if primary_artist != artist_name:
        logger.info(f"Extracted {primary_artist} as primary artist name for {artist_name}")

    return primary_artist


def search_for_track(track_name, artist_name: str, year, skip_imperfect_matches=False):
    # TODO be smarter about this - use featured artist to match if multiple artists returned from Spotify
    artist_name = get_primary_artist_name(artist_name)

    query = f"{track_name} {artist_name}"
    results = sp.search(query)
    if results["tracks"] and results["tracks"]["items"]:
        for track in results["tracks"]["items"]:
            # TODO better matching on things like "Life Is Good (feat. Drake)", when query is "Life Is Good"
            # TODO Señorita → Senorita - or just clean up input file to have ñ
            # TODO match Beyoncé from Beyonce
            # TODO match Kesha from Ke$ha
            if track["name"].lower() == track_name.lower() or track_name.lower() in track["name"].lower():
                if len(track["artists"]) == 0:
                    return track

                if "remaster" in track["name"].lower() or "remaster" in track["album"]["name"].lower():
                    # Spotify keeps the original release date for remasters
                    continue

                for artist in track["artists"]:
                    if get_primary_artist_name(artist["name"].lower()) == artist_name.lower():
                        logger.info(f"For {track_name} by {artist_name}, found {track['name']} by {artist['name']}")
                        return track

        if skip_imperfect_matches:
            return

        # prompt to choose a track
        choices_dict = {}
        for track in results["tracks"]["items"]:
            if not is_possible_year_match(track, year):
                continue

            # TODO filter out remasters not matching this pattern
            # Michael Jackson's "Thriller 25 Deluxe Edition" was released in 2008 but Spotify has 1983. Only note of 2008 is in copyright
            if "remaster" in track["name"].lower() or "remaster" in track["album"]["name"].lower():
                continue

            message = f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])} ({track['album']['release_date']})"
            choices_dict[message] = track["id"]

        if not choices_dict:
            logger.warning(f"Found no tracks for {track_name} by {artist_name}")
            return

        none_of_the_above = "None of the above"
        questions = [
            inquirer.List("track", message=f"Which track best matches {track_name} by {artist_name} ({year})?", choices=list(choices_dict.keys()) + [none_of_the_above])
        ]
        chosen = inquirer.prompt(questions)
        if chosen["track"] == none_of_the_above:
            return

        chosen_track_id = choices_dict[chosen["track"]]
        return list(track for track in results["tracks"]["items"] if track["id"] == chosen_track_id)[0]
    else:
        logger.warning(f"Found no tracks for {track_name} by {artist_name}")

        # else
        # fuzzy match on track name + artist name?
        # filter by release date closest to and prior to year?

def is_possible_year_match(track, year):
    """
        Returns true if the track was released by the time it was on the Billboard chart
        Plus some fuzzy matching
    """
    release_date = track["album"]["release_date"]
    release_date_precision = track["album"]["release_date_precision"]
    if release_date_precision == 'day':
        release_date_format = '%Y-%m-%d'
    elif release_date_precision == 'month':
        release_date_format = '%Y-%m'
    elif release_date_precision == 'year':
        release_date_format = '%Y'
    else:
        logger.warn(f"Could not determine release date format: f{release_date}, precision is f{release_date_precision}")

    release_date = datetime.datetime.strptime(release_date, release_date_format)
    end_of_billboard_year = datetime.datetime(year, 12, 31)

    return release_date < end_of_billboard_year

def get_track_info(name, artist):
    query = '%s %s' % (name, artist)
    return sp.search(q=query)


def get_artist(id):
    return sp.artist(id)


def get_track(id):
    return sp.track(id)


def get_audio_analysis(track_id):
    return sp.audio_analysis(track_id)


if __name__ == "__main__":
    results = sp.search('Creep Radiohead')
    logger.info(results['tracks']['items'])
