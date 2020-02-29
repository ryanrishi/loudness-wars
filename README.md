loudness wars
===

This repository contains the code for a personal project I'm working on. The loudness wars refers to the decreasing dynamic range of the music industry. The overall loudness of popular music is increasing because record labels are adding increasing amounts dynamic compression.

Feel free to clone this repo and see for yourself&mdash;just feed `loudness_wars.py` a CSV file track titles and artists, and the program will output a CSV file with the overall loudness (among other attributes) of each song.

# Usage
## virtualenv
```
source venv/bin/activate
```

## config
Register for a Spotify developer account [here](https://developer.spotify.com/dashboard). Get the `client_id` and `client_secret` and put them in a file named `config` (see `example.config` for an example config).

## Run it
Add some songs (track title / artist) to `in.csv`.
```
python main.py
```
