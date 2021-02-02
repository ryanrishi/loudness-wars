import sqlite3
import logging
from os import path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_db_connection(database="spotify"):
    try:
        conn = sqlite3.connect(path.join(path.dirname(__file__), f"{database}.db"))
        return conn
    except Exception as e:
        logger.error(f"Error creating database connection: {e}")


def dict_factory(cursor, row):
    """
        See https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
