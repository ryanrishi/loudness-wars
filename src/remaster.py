from client import get_track_info
from billboard import billboard_by_year
from fuzzywuzzy import fuzz

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
    print "find_remaster(%d, %s, %s, %s)" % (len(results), name, artist, year)
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
    for track in tracks:
        song = "%s remaster" % track['Song Title']
        artist = track['Artist']
        results = get_track_info(song, artist)
        remaster = find_remaster(results, song, artist, year)
        import json
        print json.dumps(remaster)
        if remaster:
            print "=== remaster: %s" % remaster["name"]
            print "=== loudness: %d" % remaster["loudness"]
        else:
            print "No remaster found for %s by %s" % (song, artist)


# if __name__ == "__main__":
#     song = "Hey Jude"
#     artist = "The Beatles"
#     year = 1968
# 
#     # original release date: 26 August 1968
#     # remaster 2015 https://open.spotify.com/album/5ju5Ouzan3QwXqQt1Tihbh
# 
#     song = "%s remastered" % song
# 
#     results = get_track_info(song, artist)
#     remaster = find_remaster(results, song, artist, year)
#     print remaster
