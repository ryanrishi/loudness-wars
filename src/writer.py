import csv

PATH_PREFIX = 'out/'


def write_results_to_file(filename, results):
    """
    
    """
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