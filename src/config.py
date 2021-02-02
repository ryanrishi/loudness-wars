import configparser
from os import path

config = configparser.ConfigParser()
config.read(path.join(path.dirname(path.dirname(__file__)), "config"))
