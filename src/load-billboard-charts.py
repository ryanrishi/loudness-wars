import csv

START_YEAR = 1950
END_YEAR = 2015

# year --> [ top song, second top song, etc. ]
billboard_by_year = {}


def load_billboard_charts():
    for year in xrange(START_YEAR, END_YEAR + 1):
        with open('billboard/%s.csv' % year, 'rU') as file:
            reader = csv.reader(file)

            # skip header
            next(reader)

            billboard_by_year[year] = list(reader)


load_billboard_charts()


if __name__ == '__main__':
    print billboard_by_year