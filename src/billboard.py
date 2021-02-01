import glob
import re
import csv
import logging
import requests
import argparse
from bs4 import BeautifulSoup
from time import sleep
from os import path

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def scrape_billboard_charts(start_year, end_year):
    for year in range(start_year, end_year + 1):
        outfile_path = get_csv_outfile(year)
        logger.info(outfile_path)
        if path.exists(outfile_path):
            logger.warning(f"{outfile_path} exists, skipping")
            continue

        success = False
        while not success:
            logger.info(f"Getting Billboard chart for {year}")
            response = requests.get(f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs")

            if response.status_code == 200:
                process_chart_html(response.text, year)
                success = True
            elif response.status_code == 429:
                # oops sorry Billboard
                logger.info("Received 429 from Billboard")

                delay = int(response.headers['Retry-After']) if response.headers['Retry-After'] is not None else 60
                logger.debug(f"Sleeping for {delay} seconds")
                sleep(delay)
            else:
                logger.error(f"Unhandled status code: {response.status_code}")


def process_chart_html(chart_html: str, year: int):
    soup = BeautifulSoup(chart_html, "html.parser")
    year_end_chart_items = soup.find_all(class_="ye-chart-item")

    fieldnames = ['rank', 'artist', 'song']
    with open(get_csv_outfile(year), "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for chart_item in year_end_chart_items:
            row = {
                "rank": int(chart_item.find(class_="ye-chart-item__rank").text),
                "artist": chart_item.find(class_="ye-chart-item__artist").text.strip(),
                "song": chart_item.find(class_="ye-chart-item__title").text.strip()
            }

            writer.writerow(row)

    logger.info(f"Processed Billboard chart for {year}")


def get_csv_outfile(year: int) -> str:
    return path.join(path.dirname(path.dirname(__file__)), f"billboard/{year}.csv")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape Billboard charts.')
    parser.add_argument('--start-year', help='The start year', default=1970)    # Billboard doesn't have charts < 1970
    parser.add_argument('--end-year', help='The end year', default=2020)

    args = parser.parse_args()
    scrape_billboard_charts(args.start_year, args.end_year)
