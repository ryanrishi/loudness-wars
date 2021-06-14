CREATE TABLE IF NOT EXISTS track (
  id TEXT NOT NULL PRIMARY KEY,
  name TEXT NOT NULL,
  position INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS artist (
  id TEXT NOT NULL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS track_artist_join (
  track_id TEXT NOT NULL,
  artist_id TEXT NOT NULL,
  FOREIGN KEY (track_id) REFERENCES track(id),
  FOREIGN KEY (artist_id) REFERENCES artist(id)
  UNIQUE (track_id, artist_id)
);

CREATE TABLE IF NOT EXISTS audio_analysis (
  track_id TEXT NOT NULL,
  analysis BLOB NOT NULL,
  FOREIGN KEY (track_id) REFERENCES track(id)
);

CREATE TABLE IF NOT EXISTS album (
  id TEXT NOT NULL PRIMARY KEY,
  name TEXT NOT_NULL,
  release_date TEXT NOT NULL,  -- can't use DATE because some release dates are just year or year + month
  release_date_precision NOT NULL
);

CREATE TABLE IF NOT EXISTS track_album_join (
  track_id TEXT NOT NULL,
  album_id TEXT NOT NULL,
  FOREIGN KEY (track_id) REFERENCES track(id),
  FOREIGN KEY (album_id) REFERENCES album(id),
  UNIQUE (track_id, album_id)
);
