setwd('~/Documents/Loudness Wars/')
source('http://bioconductor.org/biocLite.R')
biocLite('rhdf5')
library(rhdf5)

# Build the CSV
all_files <- list.files(path = './MillionSongSubset/data/')
data = data.frame()
for (file in all_files) {
    
}
h5ls('./MillionSongSubset/data/A/A/A/TRAAAAW128F429D538.h5')
data <- h5read('./MillionSongSubset/data/A/A/A/TRAAAAW128F429D538.h5', name = 'TRAAAAW128F429D538')
h5re




# new
install.packages('RCurl')
library(RCurl)
library(stringr)

CLIENT_ID = '2a38d0e861c249178c789e6a9ee937bf'
CLIENT_SECRET = 'ebe7a4e259804c1a8fa79a2b01624791'

# OAuth
req <- POST("https://api.spotify.com/authorize",
            add_headers(
              "Authorization" = paste("Basic", CLIENT_SECRET),
              "Content-Type" = "application/x-www-form-urlencoded;charset=UTF-8"
            )
)
token = NULL

# test API call
q = 'moderat+last+time'
GET(paste('https://api.spotify.com/v1/search?q=', q,'&type=', 'artist,track', sep = ''), add_headers(Authorization = token) )
