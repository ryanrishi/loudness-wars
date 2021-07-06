loudness wars
===

The loudness wars refers to the decreasing dynamic range of the music industry. The overall loudness of popular music is increasing because producers are adding increasing amounts dynamic compression.

Feel free to clone this repo and see for yourself&mdash;just feed `loudness_wars.py` a CSV file with track titles and artists, and the program will output a CSV file with the overall loudness (among other attributes) of each song.

Note 3/1/2020: Found a dataset similar to what I'm looking at saving data.world
- https://data.world/kcmillersean/billboard-hot-100-1958-2017/workspace/project-summary?agentid=kcmillersean&datasetid=billboard-hot-100-1958-2017
- https://mydatamusingsblog.wordpress.com/2017/07/20/more_metal/

# Usage
## `virtualenv`
```sh
$ virtualenv venv
$ source venv/bin/activate
```

## `pip`
```sh
$ pip install -r requirements.txt
```

## config
Register for a Spotify developer account [here](https://developer.spotify.com/dashboard). Get the `client_id` and `client_secret` and put them in a file named `config` (see `example.config` for an example config).

## Run it
Add some songs (track title / artist) to `in.csv`.
```sh
$ python loudness_wars.py
```


Eventually, I want to end up with a CSV that has:
```
year  title   artist  album track_id  loudness genre  album_artwork_url
```

And store:
- `tracks/{{track_id}}.json` - results from `GET /tracks/:track_id`
- `analysis/{{track_id}}.json` - results from `GET /audio-analysis/:track_id`
