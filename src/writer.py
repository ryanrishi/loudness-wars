import csv

PATH_PREFIX = 'out/'


def format_row_for_remaster_csv(track_info, loudness, is_remaster=False):
    # loudness comes from audio_analysis, everything else if from track
    # song, artist, release_date (OG/remaster), remaster (y/n), loudness, track_id
    row = {
        "song": track_info["name"],
        "artist": ', '.join(artist["name"] for artist in track_info["artists"]),
        "release_date": track_info["album"]["release_date"],
        "is_remaster": is_remaster,
        "loudness": loudness,
        "track_id": track_info["id"]
    }
    
    return row


def write_results_to_file(filename, results):
    filename = "%s%s" % (PATH_PREFIX, filename)
    with open(filename, "w+") as f:
        fieldnames = ['Position', 'Song Title', 'Artist', 'Loudness']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)


if __name__ == "__main__":
    print "Testing CSV writer"
    results = [
        {
            "Position": 1,
            "Song Title": "Electric Bugaloo",
            "Artist": "Some Artist",
            "Loudness": -10.1234
        },
        {
            "Position": 1,
            "Song Title": "Second Place",
            "Artist": "asdf",
            "Loudness": -8
        }
    ]
    
    filename = "test.csv"
    write_results_to_file(filename, results)
    print "Wrote results to %s" % filename