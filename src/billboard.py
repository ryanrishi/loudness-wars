import glob
import re
import csv


# year --> [ top song, second top song, etc. ]
billboard_by_year = {}


def load_billboard_charts():
    for file in glob.glob('billboard/*.csv'):
        with open(file, 'rU') as f:
            reader = csv.DictReader(f)
            year = re.search('(\d+)', file).group(0)
            billboard_by_year[year] = list(reader)


load_billboard_charts()


if __name__ == '__main__':
    print billboard_by_year
