# A script to retrieve metadata from AniList for Komga.

import requests, json

import config

# Welcome
print("Welcome to the BooksAPI metadata retreiver\n")
print("------\n")

# Initiate Session:

print("Logging in with "+config.user+" to "+config.baseURL)

# Initiate & configure session
session = requests.Session()

session.auth(config.user, config.passwd)
session.headers.update({
	"Content-Type":"application/json",
	})

# Retrieve list of series from Komga

try:
	response = session.get(config.baseURL+"/api/v1/series?size=10")
	response.raise_for_status()
	content = response.json()
	print("The request was a success!")

	print(type(response.json()))
	print("\n ------ \n")
	print(response.json().keys())

	

except requests.exceptions.HTTPError as errh:
	print(errh)
	sys.exit(1)
except requests.exceptions.ConnectionError as errc:
	print(errc)
	sys.exit(1)
except requests.exceptions.Timeout as errt:
	print(errt)
	sys.exit(1)
except requests.exceptions.RequestException as err:
	print(err)
	sys.exit(1)

# Loop to look up per library series

