# A script to retrieve metadata from AniList for Komga.

import requests, json

# Initiate Session:

# Initiate & configure session
session = requests.Session() 
session.headers.update({
	"Content-Type":"application/json",
	"x-api-key":config.apiKey,
	})

# Retrieve list of series from Komga



# Loop to look up per library series

