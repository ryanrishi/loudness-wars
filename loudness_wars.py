import spotipy
from time import sleep
import csv
import socket

sp = None

"""
    TODO
    - get metadata for song (year, album, record label?)
    - in get_loudness:
        - if no match, track title should change too
    - remastered albums - louder?

    THINGS TO COMPARE
    - loudness, year, chart position, genre
"""

TRACKS = []

EMPTY_RESULTS = {
    'time_signature': '',
    'analysis_url': '',
    'energy': '',
    'liveness': '',
    'tempo': '',
    'speechiness': '',
    'acousticness': '',
    'danceability': '',
    'instrumentalness': '',
    'key': '',
    'duration': '',
    'loudness': '',
    'audio_md5': '',
    'valence': '',
    'mode': ''
}

EMPTY_META_RESULTS = {
    'album_id': '',
    'album_name': '',
    'release_date': '',
    'genres': []
}


def get_audio_summary(title='', artist=''):
    # print title, artist
    try:
        res = pyechonest.song.search(title=title, artist=artist)
        if not res:
            print 'No results found for %s by %s' % (title, artist)
            return EMPTY_RESULTS
        if not res[0].title.lower() == title.lower():
            # Go through results and see if there is a match
            for i in range(len(res)):
                if res[i].title.lower() == title.lower():
                    return res[i].audio_summary
            print 'No results found for %s by %s' % (title, artist)
            return EMPTY_RESULTS
            # No exact match found --> prompt for user to choose one of the results
            # print 'Song title doesn\'t match. Searched for %s, found %s' % (title, res[0].title)
            # for i in range(len(res)):
            #     print '%d\t%s' % (i, res[i].title)
            # try:
            #     selected = int(raw_input('Which song would you like to search for (0 - %d, or newline to skip)? ' % (len(res) - 1)))
            # except ValueError:
            #     return
            # return res[selected].get_audio_summary()
        return res[0].audio_summary
    except pyechonest.util.EchoNestAPIError as e:
        # Handles rate limiting, but also happens when title/artist isn't UTF-8
        print title, artist, e
        print 'Sleeping for 60 seconds...'
        sleep(60)
        return get_audio_summary(title, artist)
    except socket.timeout:
        print 'Socket timed out. Trying again.'
        return get_audio_summary(title, artist)


# TODO need to clean up exception handling/if no results found
# TODO genres: pyechonest.artist.Arist(artist_id), a.get_attribute('genres')
def get_track_metadata(title='', artist=''):
    # print title, artist
    meta = {}
    res = sp.search(title + ' ' + artist)
    # Get album for this track
    if not res:
        return EMPTY_META_RESULTS
    for track in res['tracks']['items']:
        if track['name'].lower() == title.lower():
            meta['album_id'] = track['album']['id']
            meta['album_name'] = track['album']['name']
            break
    if not meta:
        return EMPTY_META_RESULTS
    # Get album genres, release date
    album_id = meta['album_id']
    res = sp.album(album_id)
    meta['genres'] = res['genres']
    meta['release_date'] = res['release_date']
    return meta


# This will return one genre. I may want to make this return a few genres with various weights
def get_artist_genres(artist=''):
    artist_name = artist
    try:
        artists = pyechonest.artist.search(artist)
        artist_id = None
        for a in artists:
            if a.name.lower() == artist.lower():
                artist_id = a.id
        # TODO fuzzy matching for artists and song titles
        if not artist_id:
            return []
        artist = pyechonest.artist.Artist(artist_id)
        if not artist.terms:
            return []
        genres = []
        for i, t in enumerate(artist.terms):
            genres.append(t['name'])
        return genres
    except pyechonest.util.EchoNestAPIError as e:
        # Handles rate limiting, but also happens when title/artist isn't UTF-8
        print artist, e
        print 'Sleeping for 60 seconds...'
        sleep(60)
        return get_artist_genres(artist_name)
    except socket.timeout:
        print 'Socket timed out. Trying again.'
        return get_artist_genres(artist_name)


def main():
    # Set EchoNest API key
    import ConfigParser
    config_parser = ConfigParser.ConfigParser()
    config_parser.readfp(open(r'config'))
    pyechonest.config.ECHO_NEST_API_KEY = config_parser.get('config', 'ECHO_NEST_API_KEY')

    # Set up Spotify wrapper
    # global sp
    # sp = spotipy.Spotify()

    # year = 2015
    # with open('input.csv', 'rU') as f:
    #     reader = csv.DictReader(f)
    #     # headers = reader.next()
    #     for row in reader:
    #         track = {
    #             'title': row['title'],
    #             'artist': row['artist'],
    #             'year': year
    #         }
    #         title = track['title'].split('feat')[0].split('!')[0]   # EchoNest API can be picky
    #         artist = track['artist'].split('feat')[0].split('and')[0]
    #         print title, artist
    #
    #         summary = get_audio_summary(title, artist)
    #         for key in summary.keys():
    #             track[key] = summary[key]
    #
    #         genres = get_artist_genres(artist)
    #         track['genres'] = genres
    #
    #         # meta = get_track_metadata(title, artist)
    #         # for key in meta.keys():
    #         #     track[key] = meta[key]
    #
    #         # print track
    #
    #         TRACKS.append(track)

    for year in xrange(1950, 2015+1):
        print year
        with open('billboard/%s.csv' % str(year), 'rU') as f:
            reader = csv.DictReader(f)
            # headers = reader.next()
            for row in reader:
                track = {
                    'position': row['Position'],
                    'title': row['Song Title'],
                    'artist': row['Artist'],
                    'year': year
                }
                title = track['title'].split('feat')[0].split('!')[0]   # EchoNest API can be picky
                artist = track['artist'].split('feat')[0].split('and')[0]
                print title, artist

                summary = get_audio_summary(title, artist)
                for key in summary.keys():
                    track[key] = summary[key]

                    track['genres'] = get_artist_genres(artist)

                # meta = get_track_metadata(title, artist)
                # for key in meta.keys():
                #     track[key] = meta[key]

                # print track

                TRACKS.append(track)

    # # print TRACKS
    # for track in TRACKS:
    #     title = track['title'].split('feat')[0].split('!')[0]    # EchoNest API can be picky
    #     artist = track['artist'].split('feat')[0]
    #     print title, artist
    #     summary = get_audio_summary(title, artist)
    #     if summary:
    #         for key in summary.keys():
    #             track[key] = summary[key]
    #     # print track

    # TODO change to DictWriter
    with open('output.csv', 'w') as f:
        # First need to change genres from array ['a', 'b', 'c'] to "a,b,c". Not sure if this is the best way to do this
        for track in TRACKS:
            track['genres'] = ','.join(track['genres'])

        fieldnames = TRACKS[0].keys()
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for track in TRACKS:
            writer.writerow(track)

main()

"""
    # Get some data
    for track in TRACKS:
        print track
        track['loudness'] = get_loudness(track['title'], track['artist'])

    print TRACKS
   """