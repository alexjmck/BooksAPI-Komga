# A script to retrieve metadata from AniList for Komga.

import requests, json

import sanitizeName as sn

import metaRetrieval as mr

from classes import *

# import config.py under verification

# Verify config file
try:
    from config import *
except ImportError:
    print("Failed to find config.py, does it exist?")
    sys.exit(1)


# Welcome
print("Welcome to the BooksAPI metadata retreiver\n")
print("------\n")



# Initiate Session:

print("Logging in with "+user+" to "+baseURL+"\n")

# Initiate & configure session
session = requests.Session()

session.auth = (user, passwd)
session.headers.update({
	"Content-Type":"application/json",
	})

# Retrieve list of series from Komga

try:
	response = session.get(baseURL+"/api/v1/series?size=5")
	response.raise_for_status()
	content = response.json()
	print("Login to Komga sucessful!\n")

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

for series in content["content"]:
	
	currentSeries = Series(series["id"], series["name"])

	mr.lookupSeries(currentSeries)

	# print(series["id"]+ series["name"])
	# seriesName = sn.sanitizeName(series["name"])
	# print(series["metadata"])
	# print("\n")

