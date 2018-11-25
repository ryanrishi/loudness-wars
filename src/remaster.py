from client import get_track_info, get_track_analysis
from billboard import billboard_by_year
from fuzzywuzzy import fuzz
from writer import format_row_for_remaster_csv
import json

# disable SSL warnings
import requests
requests.packages.urllib3.disable_warnings()


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



if DEBUG:
    print "DEBUG is True"
    song = "Hey Jude"
    artist = "The Beatles"
    year = 1968

    # original release date: 26 August 1968
    # remaster 2015 https://open.spotify.com/album/5ju5Ouzan3QwXqQt1Tihbh
    
    # Another good one is Jailhouse Rock - 2003 Sony Remaster

    song = "%s remastered" % song
    
    print "Song to find:\t%s" % song

    results = get_track_info(song, artist)
    remaster = find_remaster(results, song, artist, year)
    print "Remaster:\t%s by %s" % (remaster["name"], remaster["artists"][0]["name"])
    analysis = get_track_analysis(remaster["id"])
    print "Loudness:\t%d" % analysis["loudness"]
    formatted = format_row_for_remaster_csv(remaster, analysis["loudness"], is_remaster=True)
    print json.dumps(formatted, indent=True, sort_keys=True)
else:
    remasters = []
    for year, tracks in billboard_by_year.iteritems():
        print 'year: %s' % year
        for track in tracks:
            song = "%s remaster" % track['Song Title']
            artist = track['Artist']
            results = get_track_info(song, artist)
            remaster = find_remaster(results, song, artist, year)
            if remaster:
                print "Remaster:\t%s" % remaster["name"]
                analysis = get_track_analysis(remaster["id"])
                print "Loudness:\t%d" % analysis["loudness"]
                # TODO append to CSV file. Store both original and remastered
