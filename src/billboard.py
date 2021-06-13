import logging
import requests
import argparse
from bs4 import BeautifulSoup
from time import sleep
from os import path
from db import get_db_connection, dict_factory
import coloredlogs

coloredlogs.install()
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def scrape_billboard_charts(start_year, end_year):
    for year in range(start_year, end_year + 1):
        success = False
        while not success:
            logger.info(f"Getting Billboard chart for {year}")
            response = requests.get(f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs")

            if response.status_code == 200:
                process_chart_html(response.text, year)
                success = True
            elif response.status_code == 429:
                # oops sorry Billboard
                delay = int(response.headers['Retry-After']) if response.headers['Retry-After'] is not None else 60
                logger.info(f"Received 429 from Billboard - sleeping for {delay} seconds")
                sleep(delay)
            else:
                logger.error(f"Unhandled status code: {response.status_code}")


def process_chart_html(chart_html: str, year: int):
    soup = BeautifulSoup(chart_html, "html.parser")
    year_end_chart_items = soup.find_all(class_="ye-chart-item")

    for chart_item in year_end_chart_items:
        track_name = chart_item.find(class_="ye-chart-item__title").text.strip()
        artist_name = chart_item.find(class_="ye-chart-item__artist").text.strip()
        rank = int(chart_item.find(class_="ye-chart-item__rank").text)
        save_song(track_name, artist_name, year, rank)

    logger.info(f"Processed Billboard chart for {year}")


def save_song(track_name, artist_name, year, rank):
    conn = get_db_connection("billboard")
    cursor = conn.cursor()

    cursor.execute('''
            SELECT * FROM chart WHERE song = ? AND artist = ? AND year = ? AND position = ?
        ''', (track_name, artist_name, year, rank))

    found_track = cursor.fetchone()

    if found_track:
        logger.debug(f"Track already exists in database: {track_name} by {artist_name} ({year})")

    if found_track is None:
        try:
            cursor.execute('''
                    INSERT INTO chart (song, artist, year, position) VALUES (?, ?, ?, ?)
                ''', (track_name, artist_name, year, rank))
            conn.commit()
        except Exception as e:
            logger.error(f"Error inserting chart track: {track_name} by {artist_name} ({year})")
            logger.error(e)


def find_billboard_chart_track(track_name, artist_name, year):
    conn = get_db_connection("billboard")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chart WHERE song = ? AND artist = ? AND year = ?", (track_name, artist_name, year))
    return cursor.fetchone()


def find_tracks_by_year(start_year, end_year):
    """
        Returns a list of tracks between the following years. Start year is inclusive, end year is exclusive.
    """
    conn = get_db_connection("billboard")
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    cursor.execute('''
            SELECT * FROM chart WHERE year >= ? AND year < ?
        ''', (start_year, end_year))

    return cursor.fetchall()


def mark_track_as_found(track_id):
    conn = get_db_connection("billboard")
    cursor = conn.cursor()

    cursor.execute('''
            UPDATE chart SET found = ? WHERE id = ?
        ''', (1, track_id))
    conn.commit()
    logger.debug(f"Marked track as found: {track_id}")


def get_csv_outfile(year: int) -> str:
    return path.join(path.dirname(path.dirname(__file__)), f"billboard/{year}.csv")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape Billboard charts.')
    parser.add_argument('--start-year', help='The start year', default=1970)    # Billboard doesn't have charts < 1970
    parser.add_argument('--end-year', help='The end year', default=2020)

    args = parser.parse_args()
    scrape_billboard_charts(args.start_year, args.end_year)
