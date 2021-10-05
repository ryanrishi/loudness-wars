# remaster

Albums to check out
```sql
select track.id, track.name, artist.id, artist.name, album.id, album.name, album.release_date from album
join track_album_join taj on taj.album_id = album.id
join track on taj.track_id = track.id
join track_artist_join on track_artist_join.track_id = track.id
join artist on track_artist_join.artist_id = artist.id
where album.name like '%remaster%' or track.name like '%remaster%';
```

| track_id               | track_name | artist_id | artist_name | album_id | album_name | release_date |
| ---                     | ---         | --- | --- | --- | --- | --- |
| 01PjrDX13iIjeHc5iJZmb3 | Empty Garden (Hey Hey Johnny) - Remastered 2003 | 3PhoLpVuITZKcymswpck5b | Elton John | 6u0a1IJnnqEqiIamPssH7G | Jump Up! | 1982-01-01 |
| 02BsTeJE4q5gWOTt58ur5U | I Can't Tell You Why - 2013 Remaster | 0ECwFtbIWEVNwjlrfc6xoL | Eagles | 1sW1HxI9VppbiXqgFQHVCP | The Long Run (2013 Remaster) | 1979 |
| 07TnWCHrFkvF61GzJuLVt0 | Hard to Say I'm Sorry / Get Away - 2006 Remaster | 3iDD7bnsjL9J4fO298r0L0 | Chicago | 4NmlDrnZOd3ejob9PoiOd9 | Chicago 16 (Expanded & Remastered) | 1982-06-07 |
| 08rR0CdyUAzJy3053xCPPG | Undercover Of The Night - Remastered | 22bE4uQ6baNwSHPVcDxLCe | The Rolling Stones | 7qHKiPqv019NfMrTak7U2s | Undercover | 1983-11-07 |
| 0D2UIFvpE0xb5wEgWrpps2 | Sweetheart | 5l6cEOynnkfX7PS7zCMRU0 | Franke & The Knockouts | 5fQQ6TiiIyO7d6a07zYJ3t | Franke & The Knockouts (Original Recording Remastered) | 1981 |
| 0GGxVTb0UwDwdaKNjBdCn3 | Woman - Remastered 2010 | 4x1nvY2FN8jxqAFA0DA02H | John Lennon | 15q7N7Wo307mfjqR29NpjF | Double Fantasy Stripped Down | 1980-11-17 |
| 0SO4oJBmDNjniJwjlHaIhO | Infatuation - 2008 Remaster | 2y8Jo9CKhJvtfeKOsYzRdT | Rod Stewart | 16B8kK28QgKIYTb7XyLMuj | The Definitive Rod Stewart | 2008-11-17 |
| 0SO4oJBmDNjniJwjlHaIhO | Infatuation - 2008 Remaster | 3j2mQFdMfe3QMGohsX5nAB | John Guess | 16B8kK28QgKIYTb7XyLMuj | The Definitive Rod Stewart | 2008-11-17 |
| 0VV8wkOM4w78A2OHZOTzNP | Live And Let Die - 2018 Remaster | 3sFhA6G1N0gG1pszb6kk1m | Wings | 1RzrSgWinUzgsnw3oQDXOy | Red Rose Speedway (Archive Collection) | 1973-04-30 |
| 0X2ckklp0uln3TRUH7JTpN | Do You Know What I Mean | 6f07NU6NNMLQYXIABUv7z3 | Lee Michaels | 6N5fXmu5ZCmwecIw1nDOZy | 5th (Remastered) | 1971-11-20 |
| 0YveezON7jpiaHA8fnUHxN | Roundabout - 2003 Remaster | 7AC976RDJzL2asmZuz7qil | Yes | 0dZF93WHyOhTWjz5EWM7yG | Fragile (Deluxe Edition) | 1971-11-26 |
| 0ZfZaT7NByalxa6bct5G67 | (Keep Feeling) Fascination - Remastered | 1aX2dmV8XoHYCOQRxjPESG | The Human League | 02H0fLEbpeRdM8xkRk2fAU | The Very Best Of The Human League | 2005-01-01 |
| 0iINibMKtoS8duvexsqnm5 | Tusk - 2015 Remaster | 08GQAI4eElDnROBrJRGE0X | Fleetwood Mac | 1d075yQcykHjerQ2BN0ABn | Tusk (Deluxe Edition) | 1979-10-12 |
| 0ofHAoxe9vBkTCp2UQIavz | Dreams - 2004 Remaster | 08GQAI4eElDnROBrJRGE0X | Fleetwood Mac | 0BwWUstDMUbgq2NYONRqlu | Rumours (Super Deluxe) | 1977-02-04 |
| 0v0XYK0pLgsPiq5u4FKHaw | Take The Long Way Home - 2010 Remastered | 3JsMj0DEzyWc0VDlHuy9Bx | Supertramp | 1zcm3UvHNHpseYOUfd0pna | Breakfast In America (Deluxe Edition) | 1979-03-29 |
| 0wb21I1NV5uVUolRXIqlJF | Come And Get It - Remastered 2010 | 4pJCawaKSZ40EnxN0YEYw3 | Badfinger | 6uA2hir5o45vrILeqQVTbr | Magic Christian Music (Remastered 2010 / Deluxe Edition) | 1970-01-09 |
| 0yJvWbn8xQKiDZ84VN5lQG | De Do Do Do, De Da Da Da | 5NGO30tJxFlKixkPSgXcFE | The Police | 23enz9nXJhH1BR1Rm5CzDJ | Zenyatta Mondatta (Remastered 2003) | 1980-10-03 |
| 14vDlv40PzpXKBo6qmht6M | Make Me Smile (Single Version) - 2002 Remaster | 3iDD7bnsjL9J4fO298r0L0 | Chicago | 0PRgsdDXQ8QPaDUetVF7yN | Chicago II | 1970-01-26 |
| 173r99cYlRApif8GLPrLqt | The Other Guy - 24-Bit Digitally Remastered 02 | 6clbbhnIqpHnqxwtOWcilg | Little River Band | 1iZgFhl4ik5FfPxaRiv3RN | The Definitive Collection | 2002-01-01 |
| 1BZMMt9H0TheQGWQy44KmO | Only The Lonely - Remastered 1999 | 6scOultrkXrQsClcbGKM7e | The Motels | 1HRjCO61kfHWX3Atps1lQz | All Four One | 1982-04-06 |
| 1GcVa4jFySlun4jLSuMhiq | Angie | 22bE4uQ6baNwSHPVcDxLCe | The Rolling Stones | 6iVOz2hudE6dv5Yrcsw2c9 | Goats Head Soup (Remastered 2009) | 1973-08-31 |
| 1JSTJqkT5qHq8MDJnJbRE1 | Every Breath You Take | 5NGO30tJxFlKixkPSgXcFE | The Police | 5W9OT0a5iZlBr83a9WMKFY | Synchronicity (Remastered 2003) | 1983-06-17 |
| 1PehfITh0TTRx3LkDdV4h3 | Fame - 2016 Remaster | 0oSGxfWSnnOXhD2fKuz2Gy | David Bowie | 0lITGovWgaQGi42EfqcE5P | Young Americans (2016 Remaster) | 1975-03-07 |
| 1QaJWSCk3UMKLotnPCIHh1 | Brass in Pocket - 2006 Remaster | 0GByy3DcfbQwDvXGCWmzv9 | Pretenders | 6AFFu3ilmlEDz1I9ZaNOZw | Pretenders | 1980-01-11 |
| 1RaUxP6LHVAgbmLOn2naLl | Cool Change - Remastered | 6clbbhnIqpHnqxwtOWcilg | Little River Band | 6vCT1BZLicHHNWc0McAWb2 | First Under The Wire (2010 Remaster) | 1979 |
| 1TfqLAPs4K3s2rJMoCokcS | Sweet Dreams (Are Made of This) - Remastered | 0NKDgy9j66h3DLnN8qu1bB | Eurythmics | 5jNDWA19BJbE24x1UUJGRY | Sweet Dreams (Are Made Of This) | 1983-01-04 |
| 1TfqLAPs4K3s2rJMoCokcS | Sweet Dreams (Are Made of This) - Remastered | 5MspMQqdVbdwP6ax3GXqum | Annie Lennox | 5jNDWA19BJbE24x1UUJGRY | Sweet Dreams (Are Made Of This) | 1983-01-04 |
| 1TfqLAPs4K3s2rJMoCokcS | Sweet Dreams (Are Made of This) - Remastered | 7gcCQIlkkfbul5Mt0jBQkg | Dave Stewart | 5jNDWA19BJbE24x1UUJGRY | Sweet Dreams (Are Made Of This) | 1983-01-04 |
| 1TsekOo0xMKvIgKK7U6zaQ | How Much Love - Remastered | 04LIHk1SobiQwt2tlupoAV | Leo Sayer | 1d79WI0e5XKTpBymbKADDQ | Endless Flight | 1976 |
| 1oRvLqwJowH9JU0uO1iVzA | Third Rate Romance - Remastered | 5wpS6LUdQYMoAreKITVtrH | Amazing Rhythm Aces | 5ZfcBQTytv6PBbl0Q68Qg9 | Stacked Deck (Remastered) | 1975 |
| 1oht5GevPN9t1T3kG1m1GO | Fire and Rain - 2019 Remaster | 0vn7UBvSQECKJm2817Yf1P | James Taylor | 1HiG0ukRmFPN13EVcf98Jx | Sweet Baby James (2019 Remaster) | 1970-02-01 |
| 21IypW8aMJ2iUhzrXe3hKO | Get Off - Remastered | 6OWX8vOXHDmO2UxsfaJnfw | Foxy | 50yo97tgypklaU5DPZyHzd | Get Off (Remastered) | 2011-02-08 |
| 2DEEMhTiUMvkiHFdXkrKfI | Church Of The Poison Mind - Remastered 2002 | 6kz53iCdBSqhQCZ21CoLcc | Culture Club | 51NPMfa9QfxsYtqzcB2VfY | Colour By Numbers | 1983-10-01 |
| 2QSUyofqpGDCo026OPiTBQ | 1999 - 2019 Remaster | 5a2EaR3hamoenG9rDuVn8j | Prince | 34MHuXONazzgSxI0cThpAg | 1999 | 1982-10-27 |
| 2TcwEYyydQuEMJwdmSgVLD | When I Need You - Remastered | 04LIHk1SobiQwt2tlupoAV | Leo Sayer | 1d79WI0e5XKTpBymbKADDQ | Endless Flight | 1976 |
| 2XKW8CH8nRZH9cF2DNjBHN | Day After Day - Remastered 2010 | 4pJCawaKSZ40EnxN0YEYw3 | Badfinger | 0BWOueFZKxQrQWNRt20Lvc | Straight Up (Remastered 2010 / Deluxe Edition) | 1971-12-13 |
| 2YOwVfcUTRjNpcLny4UC4r | The Long Run - 2013 Remaster | 0ECwFtbIWEVNwjlrfc6xoL | Eagles | 1sW1HxI9VppbiXqgFQHVCP | The Long Run (2013 Remaster) | 1979 |
| 2bzgKuK3pVez40qUvo8sYr | Heartache Tonight - 2013 Remaster | 0ECwFtbIWEVNwjlrfc6xoL | Eagles | 1sW1HxI9VppbiXqgFQHVCP | The Long Run (2013 Remaster) | 1979 |
| 2kkvB3RNRzwjFdGhaUA0tz | Layla | 2rc78XDH9zuJP6bm78lU8Z | Derek & The Dominos | 5iIWnMgvSM8uEBwXKsPcXM | Layla And Other Assorted Love Songs (Remastered 2010) | 1970-11-01 |
| 2wSAWEYUHkt92X4SBAPqZE | Karma Chameleon - Remastered 2002 | 6kz53iCdBSqhQCZ21CoLcc | Culture Club | 51NPMfa9QfxsYtqzcB2VfY | Colour By Numbers | 1983-10-01 |
| 2zFdsAIk9r2Mi7Lmm1w3sM | That's All - 2007 Remaster | 3CkvROUTQ6nRi9yQOcsB50 | Genesis | 6BX8AS7J97PSQNrteX325Z | Genesis | 1983-10-03 |
| 31QuJZfFiMk1uOawow8ejS | Nobody Told Me - Remastered 2010 | 4x1nvY2FN8jxqAFA0DA02H | John Lennon | 1HRCspKjuNI3bGzZgvFU3y | Milk And Honey | 1984-01-27 |
| 32fKHW6Eac4yBXn9WY7Aic | All Those Years Ago - Remastered 2004 | 7FIoB5PHdrMZVC3q2HE5MS | George Harrison | 574Ws1iXSN3oLjtWyfoMZH | Somewhere In England | 1981-06-01 |
| 34D6mvDTAPypm92EPs8Rxa | Reminiscing - Remastered | 6clbbhnIqpHnqxwtOWcilg | Little River Band | 362Gq4moTnxkud6hQEKsm1 | Sleeper Catcher (Remastered) | 1978 |
| 35ItUJlMtjOQW3SSiTCrrw | Crazy Little Thing Called Love - Remastered 2011 | 1dfeR4HaWDbWqFHLkxsg1d | Queen | 6wPXUmYJ9mOWrKlLzZ5cCa | The Game (Deluxe Remastered Version) | 1980-06-27 |
| 36xEjbl8DtevPJgw6i9IuY | Feels like the First Time - 2008 Remaster | 6IRouO5mvvfcyxtPDKMYFN | Foreigner | 3RYi1mBYapOaGWQvwRjRjr | No End in Sight: The Very Best of Foreigner (Expanded) | 2008 |
| 39lSeqnyjZJejRuaREfyLL | Hungry Like the Wolf - 2009 Remaster | 0lZoBs4Pzo7R89JM9lxwoT | Duran Duran | 02tfQwJSOLP77oCd9U8bqm | Rio (Collector's Edition) | 1982-05-10 |
| 3AA2SafseoJo431Pee120g | Long Tall Glasses (I Can Dance) - Remastered | 04LIHk1SobiQwt2tlupoAV | Leo Sayer | 4U9kO19aacQAfVYdzxQ3Db | Just A Boy | 1974 |
| 3CPeWqqaHR0hmyfsWhMJQs | Don't Stop - 2004 Remaster | 08GQAI4eElDnROBrJRGE0X | Fleetwood Mac | 0BwWUstDMUbgq2NYONRqlu | Rumours (Super Deluxe) | 1977-02-04 |
| 3FD0RyHoYObYJkBIDGra4W | Sukiyaki - Remastered | 1ii6e2pv8VIRwnTER71rMl | A Taste Of Honey | 3vS1iaaaiF31hK4vNIc6iM | Classic Masters | 2002-01-01 |
| 3JpaL6FMH9kjVWMA1mTmRl | Union of the Snake - 2010 Remaster | 0lZoBs4Pzo7R89JM9lxwoT | Duran Duran | 0jBIq5EY9zRBZJuCE9iuM1 | Seven and the Ragged Tiger (Deluxe Edition) | 1983-11-21 |
| 3KPwt1LBpt1jVSHz8GXERo | Feel like Makin' Love - 2015 Remaster | 5AEG63ajney2BoDXi0Vb84 | Bad Company | 1LgPUiosPMevbB4NHxcNiO | Straight Shooter | 1975 |
| 3LMe4h7CrPLJrViTVzfDot | Wasted on the Way - 2005 Remaster | 2pdvghEHZJtgSXZ7cvNLou | Crosby, Stills & Nash | 7mepsTLhRL4ghKLZ4oB31u | Daylight Again (Deluxe Edition) | 1982-06-21 |
| 3OZ40egQbNWeTe0BnR2QKa | Lonesome Loser - Remastered | 6clbbhnIqpHnqxwtOWcilg | Little River Band | 6vCT1BZLicHHNWc0McAWb2 | First Under The Wire (2010 Remaster) | 1979 |
| 3RJ81z1sPLeWEFuCfGaCLC | More Than I Can Say - Remastered | 04LIHk1SobiQwt2tlupoAV | Leo Sayer | 7fjKXnW6bvlKkVzt6x2sZW | Living In A Fantasy | 1980 |
| 3Tows9RnoAq9CmMJaII2cO | Hard Habit to Break - 2006 Remaster | 3iDD7bnsjL9J4fO298r0L0 | Chicago | 1ICKrl6sDjJD1YdR9VDfPR | Chicago 17 (Expanded & Remastered) | 1984-05-14 |
| 3Ug96zKa29P3vICEEcYajZ | We Don't Talk Anymore - 2001 Remaster | 2nvKpWcP8etYTq4JrRiUiy | Cliff Richard | 2QV9SouhSHFNpls0Dvyoo5 | Rock 'n' Roll Juvenile | 1979 |
| 3XcjIvaZVUFAIdIYZqY9bd | We're An American Band - Remastered 2002 | 0qEcf3SFlpRcb3lK3f2GZI | Grand Funk Railroad | 6hSAjI92A6vPL6OM1DWTZg | We're An American Band (Remastered / Bonus Track) | 1973 |
| 3ZXcjz3A5vNsR5dA1e6ITl | Always Something There to Remind Me - 2018 Remaster | 3C6chBmZ9wzisBhoh8G2nK | Naked Eyes | 7HjVFnnMa4WF38J2BJqiTl | Naked Eyes (2018 Remaster) | 1983-01-01 |
| 3bIgVAJqxzUKUIg5Wj72C8 | We're An American Band | 0qEcf3SFlpRcb3lK3f2GZI | Grand Funk Railroad | 4HmWOsD5ggw9It34pM7nUf | Greatest Hits: Grand Funk Railroad (Remastered) | 2006-01-01 |
| 3cq6mwsjgygbwRIi9wVPGv | Mr. Bojangles - Remastered 2001 | 7y70dch6JuuuNnwlsOQvwW | Nitty Gritty Dirt Band | 2ZJcwgKQMSLyQAfBJsWfbD | Certified Hits (Remastered) | 2001-01-01 |
| 3fn87ydk7ihtvVr8EwjYvr | Lady - 2010 Digital Remaster | 6clbbhnIqpHnqxwtOWcilg | Little River Band | 362Gq4moTnxkud6hQEKsm1 | Sleeper Catcher (Remastered) | 1978 |
| 3hJLKtTpgct9Y9wKww0BiR | Miss You - Remastered | 22bE4uQ6baNwSHPVcDxLCe | The Rolling Stones | 1Jv2AqzhgsduUik2p4k3cS | Some Girls | 1978-06-09 |
| 3ix6K4wZY29bCujrSznwFZ | Let's Dance - 2018 Remaster | 0oSGxfWSnnOXhD2fKuz2Gy | David Bowie | 4NwG11AsDJluT732lSjMrV | Let's Dance (2018 Remaster) | 1983-04-14 |
| 3uiMBldZ07pW0ySHDX5gzE | Silly Love Songs - Remastered 2014 | 3sFhA6G1N0gG1pszb6kk1m | Wings | 3eN0kcFvDvdpjAvv1qZa4D | Wings At The Speed Of Sound (Archive Collection) | 1976-03-25 |
| 3w3rLh6wmne91BS2rwgcog | Sad Eyes - Remastered | 3pbKylceBTiUa0fZk4J4sJ | Robert John | 48PU11yPb5ZWZ7cOHDXOxo | Classic Masters | 2002 |
| 400ZJAUFuEuIGXhr7ie4xf | Wrapped Around Your Finger | 5NGO30tJxFlKixkPSgXcFE | The Police | 5W9OT0a5iZlBr83a9WMKFY | Synchronicity (Remastered 2003) | 1983-06-17 |
| 44aTAUBF0g6sMkMNE8I5kd | Every Little Thing She Does Is Magic | 5NGO30tJxFlKixkPSgXcFE | The Police | 5jkwdY6jS1Hzi8epr6HW7h | Ghost In The Machine (Remastered 2003) | 1981-10-02 |
| 4FLEKG82bHeT2olTM8E2Fy | Ooh Baby Baby - 1999 Remaster | 1sXbwvCQLGZnaH0Jp2HTVc | Linda Ronstadt | 0jJWrATAnjC1tZXPZWdWZL | Living in the USA | 1978 |
| 4IRHwIZHzlHT1FQpRa5RdE | Goodbye Yellow Brick Road - Remastered 2014 | 3PhoLpVuITZKcymswpck5b | Elton John | 5WupqgR68HfuHt3BMJtgun | Goodbye Yellow Brick Road (Remastered) | 1973-10-05 |
| 4JRem7xHp2l0kmUvt9zCKu | Golden Years - 2016 Remaster | 0oSGxfWSnnOXhD2fKuz2Gy | David Bowie | 0MWrKayUshRuT8maG4ZAOU | Station to Station (2016 Remaster) | 1976-01-23 |
| 4N1dFbXmRng8qJ3KdJrbLr | Little Red Corvette - 7" Edit - 2019 Remaster | 5a2EaR3hamoenG9rDuVn8j | Prince | 2EHUlDJaTyvn0gAvVfUlcY | 1999 (Super Deluxe Edition) | 2019-09-10 |
| 4OJFkrRQqol4FsPesF8eu4 | Saturday in the Park - 2002 Remaster | 3iDD7bnsjL9J4fO298r0L0 | Chicago | 2oSXXINsWGuEsc4udgWxh8 | Chicago V (Expanded & Remastered) | 1972-07-10 |
| 4OKf7CcYuw5H2HptkcKxcP | You're My Best Friend - Remastered 2011 | 1dfeR4HaWDbWqFHLkxsg1d | Queen | 6X9k3hSsvQck2OfKYdBbXr | A Night At The Opera (Deluxe Remastered Version) | 1975-11-21 |
| 4PFhHd7DsNg0ke9Nmlxms5 | Blue Eyes - Remastered 2003 | 3PhoLpVuITZKcymswpck5b | Elton John | 6u0a1IJnnqEqiIamPssH7G | Jump Up! | 1982-01-01 |
| 4RS9PmtHQe7I0o5fEeweOY | Dance the Night Away - 2015 Remaster | 2cnMpRsOVqtPMfq7YiFE6K | Van Halen | 3w93PGkmXAmEAdJVvmPbzI | Van Halen II (Remastered) | 1979-03-23 |
| 4Wd9pEtEnZNDjgiswGOpJb | Waiting On A Friend - Remastered 2009 | 22bE4uQ6baNwSHPVcDxLCe | The Rolling Stones | 15XNBzVWARPMlu0sEbfBjJ | Tattoo You (2009 Re-Mastered) | 1981-08-24 |
| 4XMRt4xFqLzGs4wDKkSSeu | Give Me Love (Give Me Peace On Earth) | 7FIoB5PHdrMZVC3q2HE5MS | George Harrison | 79hB4QtJjn0Y4DyRPpllZg | Living In The Material World (Remastered) | 1973-05-30 |
| 4YwbSZaYeYja8Umyt222Qf | You Can't Hurry Love - 2016 Remaster | 4lxfqrEsLX6N1N4OCSkILp | Phil Collins | 6sn6eWmPciSiHj0ltTBl7M | Hello, I Must Be Going! (Deluxe Edition) | 1982-11-05 |
| 4fKhRRYn7F5shZItjJkPJU | Watching The Wheels - Remastered 2010 | 4x1nvY2FN8jxqAFA0DA02H | John Lennon | 15q7N7Wo307mfjqR29NpjF | Double Fantasy Stripped Down | 1980-11-17 |
| 4fbwTO3DJ2qryMddov9RbB | Rhiannon (Will You Ever Win) - 2018 Remaster | 08GQAI4eElDnROBrJRGE0X | Fleetwood Mac | 06JqOkwwy91OxrApXclzYf | 50 Years - Don't Stop | 2018-11-16 |
| 4sz1Ng2Cgidfqqiy0pNL6R | The Reflex - Single Version; 2010 Remaster | 0lZoBs4Pzo7R89JM9lxwoT | Duran Duran | 0jBIq5EY9zRBZJuCE9iuM1 | Seven and the Ragged Tiger (Deluxe Edition) | 1983-11-21 |
| 4xh7W7tlNMIczFhupCPniY | Go Your Own Way - 2004 Remaster | 08GQAI4eElDnROBrJRGE0X | Fleetwood Mac | 0BwWUstDMUbgq2NYONRqlu | Rumours (Super Deluxe) | 1977-02-04 |
| 52KvuGmgcgRdrLMXOtda0E | The Stroke - Remastered | 3Fz2GbraVXhcpXnoi2Oe1r | Billy Squier | 6TwlLNU5Zd9qGuNgSLeWPt | Don't Say No | 1981 |
| 56KqaFSGTb7ifpt16t5Y1N | Rock the Casbah - Remastered | 3RGLhK1IP9jnYFH4BRFJBS | The Clash | 1ZH5g1RDq3GY1OvyD0w0s2 | Combat Rock (Remastered) | 1982 |
| 56SnVQVuJuqnYA6rLdcg32 | Miss Me Blind - Remastered 2003 | 6kz53iCdBSqhQCZ21CoLcc | Culture Club | 51NPMfa9QfxsYtqzcB2VfY | Colour By Numbers | 1983-10-01 |
| 57JVGBtBLCfHw2muk5416J | Another One Bites The Dust - Remastered 2011 | 1dfeR4HaWDbWqFHLkxsg1d | Queen | 6wPXUmYJ9mOWrKlLzZ5cCa | The Game (Deluxe Remastered Version) | 1980-06-27 |
| 5BCPL5mWm6UqI4atl18kVm | Call on Me - 2002 Remaster | 3iDD7bnsjL9J4fO298r0L0 | Chicago | 4O8dmYS0wfxvY56LJdp280 | Chicago VII (Expanded & Remastered) | 1974-03-11 |
| 5DEy8wVNCdJdAGNsOWxmVQ | It Only Takes A Minute - Remastered | 3LfO03nEZMdWNHG2tLpMa0 | Tavares | 04p4pcNAodBupBWhO2p0w8 | Anthology | 2004-01-01 |
| 5Ei9o2fHEnfHb84YrPuz4v | China Girl - 2018 Remaster | 0oSGxfWSnnOXhD2fKuz2Gy | David Bowie | 4NwG11AsDJluT732lSjMrV | Let's Dance (2018 Remaster) | 1983-04-14 |
| 5IATbFZds3cbOx8YxuMuko | Emotional Rescue - Remastered 2009 | 22bE4uQ6baNwSHPVcDxLCe | The Rolling Stones | 5mEjFOLcBs94wSchOtMCTB | Emotional Rescue (2009 Re-Mastered) | 1980-06-20 |
| 5Vrczz39CvlD3OGCa6utoA | Grease - 2007 Remaster | 3CDKmzJu6uwEGnPLLZffpD | Frankie Valli | 0o2oPAxKGui4tvrrNgDtkc | Frankie Valli...Is The Word | 1978 |
| 5Wj1rJnCLpMHdLaxsFtJLs | Bennie And The Jets - Remastered 2014 | 3PhoLpVuITZKcymswpck5b | Elton John | 5WupqgR68HfuHt3BMJtgun | Goodbye Yellow Brick Road (Remastered) | 1973-10-05 |
| 5ol5vmBHvjrdEXfky3gsQk | I Believe In You (You Believe In Me) | 4OGuNAnRFWZOgOA2d51taz | Johnnie Taylor | 3x5GGfpGdo20wuA3FpmZLC | Taylored In Silk (Remastered) | 1973 |
| 5uRkew0DtfAQmv0oEYNwFF | I Saw the Light - 2015 Remaster | 0Lpr5wXzWLtDWm1SjNbpPb | Todd Rundgren | 3zNPrWuTPDQeqdj2Y8UjO1 | Something / Anything? | 1972 |
| 5veJDT0MLsLbhYsx42GXUD | Don't Stand So Close To Me | 5NGO30tJxFlKixkPSgXcFE | The Police | 23enz9nXJhH1BR1Rm5CzDJ | Zenyatta Mondatta (Remastered 2003) | 1980-10-03 |
| 5x5FUXjs53WbPuTwT6WD8d | (She's) Sexy + 17 - Single Edit/24 Bit Remastered 99/Digital Remaster/1999 | 2ibPkysx2PXqWLmxFD7jSg | Stray Cats | 5yeIWI4LK4TzTHvFM00Zii | The Brian Setzer Collection 1981-1988 (Remastered) | 1999-01-01 |
| 5y0YreEOnQiKFAnCrcFIXz | (Just Like) Starting Over - Remastered 2010 | 4x1nvY2FN8jxqAFA0DA02H | John Lennon | 15q7N7Wo307mfjqR29NpjF | Double Fantasy Stripped Down | 1980-11-17 |
| 62NJcC5piTuieIFiDZxiz1 | With Your Love - Remastered | 3HC7NcxQx2Yk0fWoRKJ0xF | Jefferson Starship | 4K8ddhRizKn5ujEWOZ6Pkj | Spitfire (Remastered) | 1976-01-01 |
| 63CHa6rmamv9OsehkRD8oz | Against All Odds (Take a Look at Me Now) - 2016 Remaster | 4lxfqrEsLX6N1N4OCSkILp | Phil Collins | 7yZHLfxqiGPbSQLrVJljah | The Singles (Expanded) | 2016-10-14 |
| 66LhCsc06aTa2Ig7iYPDSP | Stop Draggin' My Heart Around (with Tom Petty and The Heartbreakers) - 2016 Remaster | 7crPfGd2k81ekOoSqQKWWz | Stevie Nicks | 0IomjU2bXFng4LQBYn7Het | Bella Donna (2016 Remastered) | 1981-07-27 |
| 66LhCsc06aTa2Ig7iYPDSP | Stop Draggin' My Heart Around (with Tom Petty and The Heartbreakers) - 2016 Remaster | 4tX2TplrkIP4v05BNC903e | Tom Petty and the Heartbreakers | 0IomjU2bXFng4LQBYn7Het | Bella Donna (2016 Remastered) | 1981-07-27 |
| 6IXSfTzUjEsKc9iOvDkIx4 | A Little in Love - 1987 Remaster | 2nvKpWcP8etYTq4JrRiUiy | Cliff Richard | 6IY0sC4U5enilDq1UZMGCH | Love Songs | 1981-06-15 |
| 6QYoHNLD0vpROBkBMOONtT | Some Kind Of Wonderful | 0qEcf3SFlpRcb3lK3f2GZI | Grand Funk Railroad | 0rnM4ercy0tEWazNwp7uLy | Caught In The Act (Live/Remastered) | 1975 |
| 6YLWRvxvC4VbFTuNRHeaDU | Clap For The Wolfman - 2003 Remastered | 0cQuYRSzlItquYxsQKDvVc | The Guess Who | 6RYVsMUeEr6HkhTopi6xTp | Road Food | 1974-04-01 |
| 6cFZ4PLC19taNlpl9pbGMf | Somebody To Love - Remastered 2011 | 1dfeR4HaWDbWqFHLkxsg1d | Queen | 0lmQ6rAGcChLjGXM52Qu3i | A Day At The Races (Deluxe Remastered Version) | 1976-12-10 |
| 6gTrbqZnyljwXdYQTyBkSx | You Make Me Feel Like Dancing - Remastered | 04LIHk1SobiQwt2tlupoAV | Leo Sayer | 1d79WI0e5XKTpBymbKADDQ | Endless Flight | 1976 |
| 6mHOcVtsHLMuesJkswc0GZ | The Logical Song - Remastered 2010 | 3JsMj0DEzyWc0VDlHuy9Bx | Supertramp | 1zcm3UvHNHpseYOUfd0pna | Breakfast In America (Deluxe Edition) | 1979-03-29 |
| 6n4t5iMFjHmA3ErCOLT9O8 | Promises, Promises - US Single Version / 2018 Remaster | 3C6chBmZ9wzisBhoh8G2nK | Naked Eyes | 7HjVFnnMa4WF38J2BJqiTl | Naked Eyes (2018 Remaster) | 1983-01-01 |
| 6ucfemTqUh5NjU161g4LtV | If Ever You're In My Arms Again - Remastered Version | 49iKbKGqgn8OESkW5WduX0 | Peabo Bryson | 0p3g60UoKhZlkFPzNaOqo8 | Fun Mom Dinner (Original Motion Picture Soundtrack) | 2017-08-04 |
| 6y9VZNRczyKeQihebHSMJ8 | She Blinded Me With Science - 2009 Remastered Version | 2Uz58cSxlJgefDaSikxYQ7 | Thomas Dolby | 6B0ZeHngr24VJ1MABDW2Yz | The Golden Age Of Wireless | 1982-06-29 |
| 6yLIqXX9edg1x0HZS7cZEv | The Air That I Breathe - 2008 Remaster | 6waa8mKu91GjzD4NlONlNJ | The Hollies | 17gEubRfhqZEFoYEnHVV5H | Hollies | 1974-03-01 |
| 6zV8IpLvw0tkRSVCFQJB1y | You've Got a Friend - 2019 Remaster | 0vn7UBvSQECKJm2817Yf1P | James Taylor | 3ahHxtwRwMIdHcAo0MEXxX | Mud Slide Slim and the Blue Horizon (2019 Remaster) | 1971-04-01 |
| 71GMl3Q7U4JnrTqI9kfcoN | Rock 'n' Roll Fantasy - 2009 Remaster | 5AEG63ajney2BoDXi0Vb84 | Bad Company | 1yNIJqbC4vSPFcc8mKEWZp | Desolation Angels (2009 Remaster) | 1979 |
| 72Z17vmmeQKAg8bptWvpVG | Space Oddity - 2015 Remaster | 0oSGxfWSnnOXhD2fKuz2Gy | David Bowie | 1ay9Z4R5ZYI2TY7WiDhNYQ | David Bowie (aka Space Oddity) [2015 Remaster] | 1969-11-04 |
| 73JqQIGZUZxCVfY54RSpCH | With A Little Luck - Remastered 1993 | 3sFhA6G1N0gG1pszb6kk1m | Wings | 5zh2BzO2n6tSpZe0PgZc8v | London Town | 1978-03-31 |
| 74tXc7WOWxEDZahXcyPG9D | New Moon on Monday - 2010 Remaster | 0lZoBs4Pzo7R89JM9lxwoT | Duran Duran | 0jBIq5EY9zRBZJuCE9iuM1 | Seven and the Ragged Tiger (Deluxe Edition) | 1983-11-21 |
| 75Nlnd9AJ4CYrLXgWGsuTF | How Sweet It Is (To Be Loved By You) - 2019 Remaster | 0vn7UBvSQECKJm2817Yf1P | James Taylor | 0x491s63vRDvG25x2Fzrny | Gorilla (2019 Remaster) | 1975-05-01 |
| 78RIER8V6EhrqVPOBi2GYa | Here Comes the Rain Again - Remastered Version | 0NKDgy9j66h3DLnN8qu1bB | Eurythmics | 4pGwe5BW8GVtIP8ruoa1jB | Touch (Reissue - Deluxe Edition) | 1983-11-14 |
| 78RIER8V6EhrqVPOBi2GYa | Here Comes the Rain Again - Remastered Version | 5MspMQqdVbdwP6ax3GXqum | Annie Lennox | 4pGwe5BW8GVtIP8ruoa1jB | Touch (Reissue - Deluxe Edition) | 1983-11-14 |
| 78RIER8V6EhrqVPOBi2GYa | Here Comes the Rain Again - Remastered Version | 7gcCQIlkkfbul5Mt0jBQkg | Dave Stewart | 4pGwe5BW8GVtIP8ruoa1jB | Touch (Reissue - Deluxe Edition) | 1983-11-14 |
| 7GqIDx2QVGOpd4r1fZaUUW | 25 or 6 to 4 - 2002 Remaster | 3iDD7bnsjL9J4fO298r0L0 | Chicago | 0PRgsdDXQ8QPaDUetVF7yN | Chicago II | 1970-01-26 |
| 7GqWnsKhMtEW0nzki5o0d8 | Killer Queen - Remastered 2011 | 1dfeR4HaWDbWqFHLkxsg1d | Queen | 6RJyYMIrOtx3VnNIoq31kj | Sheer Heart Attack (Deluxe Remastered Version) | 1974-11-08 |
| 7HF88mJXq8DpotZohoW2mo | She's A Beauty - Remastered 1991 | 7zfhej6FnVXN9LIXs6dcoK | The Tubes | 2WiDQ5arP6dQ5unzoTJ0UH | Outside Inside | 1983 |
| 7N3PAbqfTjSEU1edb2tY8j | Jump - 2015 Remaster | 2cnMpRsOVqtPMfq7YiFE6K | Van Halen | 3REUXdj5OPKhuDTrTtCBU0 | 1984 (Remastered) | 1984-01-04 |
| 7t6CAWplijBj4sdl0q3z0e | Legs - 2008 Remaster | 2AM4ilv6UzW0uMRuqKtDgN | ZZ Top | 5LMGAYhn2ywaxGZdtmXGpw | Eliminator | 1983-03-23 |
| 7tFiyTwD0nx5a1eklYtX2J | Bohemian Rhapsody - Remastered 2011 | 1dfeR4HaWDbWqFHLkxsg1d | Queen | 6X9k3hSsvQck2OfKYdBbXr | A Night At The Opera (Deluxe Remastered Version) | 1975-11-21 |
| 7v5rsCN3LhX9XaIlWyTdx3 | Steal Away - Remastered | 3jrgftS3TYbNxcPt5itKhz | Robbie Dupree | 1sY2wLftl601YlV9YUQFgW | Robbie Dupree | 1980-12-01 |
| 7wJpqjqk8QbHpCakY1ZacY | At Seventeen - Remastered | 5c9uFWpZY2MTlk7Rft0tgp | Janis Ian | 6RjDm4cjV3MFndKrpLUxpO | Between the Lines (Remastered) | 1975-03-01 |
