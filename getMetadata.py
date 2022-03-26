# A script to retrieve metadata from AniList for Komga.

import requests, json

import auth

# Initiate Session:

# Initiate & configure session
session = requests.Session()

session.auth(auth.user,auth.passwd)
session.headers.update({
	"Content-Type":"application/json",
	})

# Retrieve list of series from Komga



# Loop to look up per library series

