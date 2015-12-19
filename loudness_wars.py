import pyechonest.config, pyechonest.song, pyechonest.util
from time import sleep
import csv
import socket

"""
    TODO
    - generate csv of input (a few hundred rows of song title and artist)
        - billboard year-end charts?
    - get metadata for song (year, album, record label?)
    - in get_loudness:
        - if no match, track title should change too
    - get more than just loudness (key, tempo, etc)
    - split artist name by 'and' -- does that improve results?

    THINGS TO COMPARE
    - loudness, year, chart position, genre
"""

TRACKS = [
    {
        'title': 'P.Y.T.',
        'artist': 'Michael Jackson'
    },
    {
        'title': 'American Idiot',
        'artist': 'Green Day'
    }
]
TRACKS = []


def get_loudness(title='', artist=''):
    # print title, artist
    try:
        res = pyechonest.song.search(title=title, artist=artist)
        if not res:
            print 'No results found for %s by %s' % (title, artist)
            return
        if not res[0].title.lower() == title.lower():
            # Go through results and see if there is a match
            for i in range(len(res)):
                if res[i].title.lower() == title.lower():
                    return res[i].get_audio_summary()['loudness']
            print 'No results found for %s by %s'
            return
            # No exact match found --> prompt for user to choose one of the results
            print 'Song title doesn\'t match. Searched for %s, found %s' % (title, res[0].title)
            for i in range(len(res)):
                print '%d\t%s' % (i, res[i].title)
            try:
                selected = int(raw_input('Which song would you like to search for (0 - %d, or newline to skip)? ' % (len(res) - 1)))
            except ValueError:
                return
            return res[selected].get_audio_summary()['loudness']
        return res[0].get_audio_summary()['loudness']
    except pyechonest.util.EchoNestAPIError as e:
        print title, artist, e
        print 'Sleeping for 60 seconds...'
        sleep(60)
        return get_loudness(title, artist)
    except socket.timeout:
        print 'Socket timed out. Trying again.'
        return get_loudness(title, artist)


def main():
    # Set EchoNest API key
    import ConfigParser
    config_parser = ConfigParser.ConfigParser()
    config_parser.readfp(open(r'config'))
    pyechonest.config.ECHO_NEST_API_KEY = config_parser.get('config', 'ECHO_NEST_API_KEY')

    # with open('input.csv', 'rU') as f:
    #     reader = csv.reader(f, dialect=csv.excel_tab, delimiter=',')
    #     headers = reader.next()
    #     # print headers
    #     for row in reader:
    #         track = {}
    #         track['title'] = row[0]
    #         track['artist'] = row[1]
    #         TRACKS.append(track)

    for year in xrange(2007, 2015):
        with open('billboard/%s.csv' % str(year), 'rU') as f:
            reader = csv.reader(f, dialect=csv.excel_tab, delimiter=',')
            headers = reader.next()
            for row in reader:
                track = {}
                track['position'] = row[0]
                track['title'] = row[2]
                track['artist'] = row[1]
                track['year'] = year
                TRACKS.append(track)

    # # print TRACKS
    for track in TRACKS:
        title = track['title'].split('feat')[0]    # EchoNest API doesn't like feat. in song title or artist name
        artist = track['artist'].split('feat')[0]
        track['loudness'] = get_loudness(title, artist)
        # print track

    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Artist', 'Year', 'Loudness'])
        for track in TRACKS:
            writer.writerow([track['title'], track['artist'], track['year'], track['loudness']])

    # with open('output2.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['Title', 'Artist', 'Loudness'])
    #     for track in TRACKS:
    #         writer.writerow([track['title'], track['artist'], track['loudness']])

main()

"""
    # Get some data
    for track in TRACKS:
        print track
        track['loudness'] = get_loudness(track['title'], track['artist'])

    print TRACKS
   """