# A script to retrieve metadata from AniList for Komga.

import requests, json

import sanitizeName as sn

import metaRetrieval as mr

import komgaPatch as kp

from classes import *

# import config.py under verification

# Verify config file
try:
    from config import *
except ImportError:
    print("Failed to find config.py, does it exist?")
    sys.exit(1)


# Welcome
print("\n-----\n")
print("Welcome to the BooksAPI metadata retreiver\n")

# Initiate Session:

print("Logging in with "+user+" to "+baseURL)

# Initiate & configure session
session = requests.Session()

session.auth = (user, passwd)
session.headers.update({
	"Content-Type":"application/json",
	'accept': '*/*'
	})

# Retrieve list of series from Komga
numSeries = input("How many series should we retreive? it will be in alphabetical order: ")

try:
	response = session.get(baseURL+"/api/v1/series?size="+numSeries)
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

skippedSeries = []

for series in content["content"]:
	
	currentSeries = Series(series)
	# print(series["metadata"])
	# print("\n")

	aniListSeries = mr.lookupSeries(currentSeries) # passes Series class

	if aniListSeries == None:
		skippedSeries.append(currentSeries.name)
		print(currentSeries.name + " skipped")
		continue

	print("\n")
	

	try:
		kp.patchSeries(session, currentSeries, aniListSeries) # passes request session Series and anilist class
	except:
		skippedSeries.append(currentSeries.name)
		print("Update failed")
		print(currentSeries.name + "failed")

print("Library updated!\n")
if len(skippedSeries) != 0:	
	print("The following series were skipped:")
	print(skippedSeries)
else:
	print("No series skipped")

	# print(series["id"]+ series["name"])
	# seriesName = sn.sanitizeName(series["name"])
	# print(series["metadata"])
	# print("\n")

