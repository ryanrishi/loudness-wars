from client import get_track_info, get_track_analysis
from billboard import billboard_by_year
from fuzzywuzzy import fuzz
from datetime import datetime
import csv
from writer import format_row_for_remaster_csv
import json
from loudness_wars import find_track_in_results
import os

# disable SSL warnings
import requests
requests.packages.urllib3.disable_warnings()

DEBUG = True

now = datetime.now()
REMASTER_FILE = "out/remaster-%s.csv" % now.strftime("%Y-%m-%d-%H:%M")


# in:   CSV with (song, artist, year)
# out:  CSV with remastered and OG songs. store (song, artist, year, remastered [y/n], loudness, track URL)

def find_remaster(results, name, artist, year):
    """
    Search for remastered songs
    - remastered release date > OG release date
    - continue if no remaster
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


def write_remaster(remaster, remaster_audio_analysis, original, original_audio_analysis):
    """
    Sample Remaster CSV:
    "remaster" field is track id for remaster, null if this is remaster

    id  name                        artist  year    loudness    remaster
    1   Hey Jude                    Beatles 1968    -10         2
    2   Hey Jude - Remaster 2015    Beatles 2015    -7
    """
    remaster_row = format_row_for_remaster_csv(remaster, remaster_audio_analysis)
    original_row = format_row_for_remaster_csv(original, original_audio_analysis)
    original_row["remaster"] = remaster["id"]
    mode = "a" if os.path.exists(REMASTER_FILE) else "w"
    fieldnames = original_row.keys()
    with open(REMASTER_FILE, mode) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(remaster_row)
        writer.writerow(original_row)


if DEBUG:
    print "DEBUG is True"
    song = "Hey Jude"
    artist = "The Beatles"
    year = 1968

    # original release date: 26 August 1968
    # remaster 2015 https://open.spotify.com/album/5ju5Ouzan3QwXqQt1Tihbh

    # Another good one is Jailhouse Rock - 2003 Sony Remaster

    remaster_title = "%s remastered" % song

    print "Song to find:\t%s" % remaster_title

    results = get_track_info(remaster_title, artist)
    remaster = find_remaster(results, remaster_title, artist, year)
    print "Remaster:\t%s by %s" % (remaster["name"], remaster["artists"][0]["name"])
    remaster_analysis = get_track_analysis(remaster["id"])
    print "Loudness:\t%d" % remaster_analysis["loudness"]
    formatted = format_row_for_remaster_csv(remaster, remaster_analysis)
    print json.dumps(formatted, indent=True, sort_keys=True)
    print "Finding original song"
    results = get_track_info(song, artist)
    original = find_track_in_results(results, song, artist)
    print json.dumps(original, indent=True, sort_keys=True)
    original_analysis = get_track_analysis(original["id"])
    write_remaster(remaster, remaster_analysis, original, original_analysis)
else:
    remasters = []
    for year, tracks in billboard_by_year.iteritems():
        print "year: %s" % year
        for track in tracks:
            song = "%s remaster" % track["Song Title"]
            artist = track["Artist"]
            results = get_track_info(song, artist)
            remaster = find_remaster(results, song, artist, year)
            if remaster:
                print "Remaster:\t%s" % remaster["name"]
                remaster_analysis = get_track_analysis(remaster["id"])
                print "Loudness:\t%d" % remaster_analysis["loudness"]
                print "Finding original song"
                original = get_track_info(track["Song Title"])
                original_analysis = get_track_analysis(original["id"])
                write_remaster(remaster, remaster_analysis, original, original_analysis)
                # TODO append to CSV file. Store both original and remastered
