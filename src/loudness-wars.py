from client import get_track_info, get_track_analysis
from billboard import billboard_by_year
from fuzzywuzzy import fuzz
from writer import write_results_to_file

# disable SSL warnings
import requests
requests.packages.urllib3.disable_warnings()


def get_loudness_for_track(track_id):
    results = get_track_analysis(track_id)
    return results["loudness"]


def find_track_in_results(results, name, artist):
    """
        iterate over tracks, fuzzy matching on track title and artist
        choose track with highest ratio for name/artist
        TOOD consider weighting by release date, in case there are rereleases/remasters
    """
    found = None
    found_name_ratio = 0
    found_artist_ratio = 0
    for track in results["tracks"]["items"]:
        name_ratio = fuzz.ratio(track["name"], name)
        for found_artist in track["artists"]:
            artist_ratio = fuzz.ratio(found_artist["name"], artist)
            if (artist_ratio > found_artist_ratio) and (name_ratio > found_name_ratio):
                found = track
                found_name_ratio = name_ratio
                found_artist_ratio = artist_ratio
    return found


for year, tracks in billboard_by_year.iteritems():
    print "=== Starting year %s ===" % year
    for track in tracks:
        rank = track['Position']
        artist = track['Artist']
        song = track['Song Title']
        print "Getting track info for %s by %s" % (song, artist)
        results = get_track_info(song, artist)
        found = find_track_in_results(results, song, artist)
        if not found:
            print "Could not find track %s by %s" % (song, artist)
        else:
            print "Searched for %s - %s" % (song, artist)
            print "Found %s - %s" % (found["name"], ' / '.join([a["name"] for a in found["artists"]]))
            loudness = get_loudness_for_track(found["id"])
            print "Loudness: %d" % loudness
            print track
            track["Loudness"] = loudness
            track["id"] = found["id"]

    filename = "%s-results.csv" % year
    write_results_to_file(filename, tracks)
