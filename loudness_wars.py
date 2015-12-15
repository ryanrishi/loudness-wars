import pyechonest.config, pyechonest.song

"""
    TODO
    - generate csv of input (a few hundred rows of song title and artist)
    - figure out rate limiting - pausing for 60 seconds every 20 requests should work
    - get metadata for song (year, album, record label?)
"""


def get_loudness(title='', artist=''):
    res = pyechonest.song.search(title=title, artist=artist)
    if len(res) == 0:
        print 'No song found'
        return
    return res[0].get_audio_summary()['loudness']


def main():
    # Set EchoNest API key
    import ConfigParser
    config_parser = ConfigParser.ConfigParser()
    config_parser.readfp(open(r'config'))
    pyechonest.config.ECHO_NEST_API_KEY = config_parser.get('config', 'ECHO_NEST_API_KEY')
    # Get some data
    print get_loudness('P.Y.T', 'Michael Jackson')
    print get_loudness('American Idiot', 'Green Day')

main()