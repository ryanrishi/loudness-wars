CREATE TABLE IF NOT EXISTS chart (
  id INTEGER NOT NULL PRIMARY KEY,
  song TEXT NOT NULL,
  artist TEXT NOT NULL,
  position INTEGER NOT NULL,
  year INTEGER NOT NULL,
  found INTEGER,  -- null/1 for boolean
  UNIQUE (position, year)
);
