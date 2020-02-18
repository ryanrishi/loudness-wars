import glob
import re
import csv
from datetime import datetime

now = datetime.now()
RESULTS_DIR = 'out/'
OUT_FILE = '%s/all-%s.csv' % (RESULTS_DIR, now.strftime('%Y-%m-%d-%H:%M'))


"""
    In hindsight, it would have been smart to have one results file
    and append rows to that. Row would have:
    - year
    - title
    - artist
    - loudness
    - rank (not really needed)

    But alas, I did not do that.

    This reads all of the results files (each file is one year) and munges
    it into one results file with the above format. So for 50 years, there
    should be about 50 year * 100 tracks/year = 5000 tracks
"""

with open(OUT_FILE, 'w') as results_file:
    fieldnames = ['Year', 'Position', 'Song Title', 'Artist', 'Loudness']
    writer = csv.DictWriter(results_file, fieldnames=fieldnames)
    writer.writeheader()

    files = glob.glob('%s*-results.csv' % RESULTS_DIR)

    for file in glob.glob('%s*-results.csv' % RESULTS_DIR):
        with open(file, 'r') as f:
            year = re.search('(\d+)', file).group(0)
            print "Processing %s" % year
            reader = csv.DictReader(f)
            for row in reader:
                if row['Loudness']:
                    row['Year'] = year
                    writer.writerow(row)

    print "Done"
