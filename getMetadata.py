# A script to retrieve metadata from AniList for Komga.

# TODO:
# Read direection for NOVEL type from anilist
# Add anilist id to series metadata as URLs
# Add MAL id to series metadata as URLs

import requests, sys

import metaRetrieval as mr

import komgaPatch as kp

from classes import *

# import config.py under verification

# Variables declarations

numSeries = None # Number of series to retrieve

ignoreLock = None # Whether to ignore field locks

skipLock = None # Whether to skip series with field locks

orderRetrieved = 0 # Order to retrieve series 

skippedSeries = [] # List of series that were skipped

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
print(" ")

while True:
	try:
		numSeries = int(input("How many series should we retreive?: "))
		break
	except:
		pass

orderOptions = {
	1: "?",
	2: "/new?",
	3: "/updated?"
}

print("What order should the library be retrieved in?")
print(" 1) Alphabetical Order")
print(" 2) Most recently added")
print(" 3) Most recently updated")

while True:
	orderRetrieved = input("Enter 1, 2, or 3:")
	# print(orderRetrieved)
	try:
		orderRetrieved = int(orderRetrieved)
	except:
		continue
	if orderRetrieved in range(4):
		break
	else:
		print("try again")

try:
	response = session.get(baseURL+"/api/v1/series"+orderOptions[orderRetrieved]+"size="+str(numSeries))
	response.raise_for_status()
	content = response.json()
	print("Login to Komga sucessful!\n")

except requests.exceptions.HTTPError as errh:
	print(errh)
	print("Error connecting to Komga Instance")
	sys.exit(1)
except requests.exceptions.ConnectionError as errc:
	print(errc)
	print("Error connecting to Komga Instance")
	sys.exit(1)
except requests.exceptions.Timeout as errt:
	print(errt)
	print("Error connecting to Komga Instance")
	sys.exit(1)
except requests.exceptions.RequestException as err:
	print(err)
	print("Error connecting to Komga Instance")
	sys.exit(1)

# Loop to look up per library series

ignoreLockDict = {
	"y": True,
	"n": False,
}

while True:
	try:
		ignoreLock = ignoreLockDict[input("Override field locks? (y/n): ")]
		break
	except:
		pass

while True:
	try:
		skipLock = ignoreLockDict[input("Skip series with field locks? (y/n): ")]
		break
	except:
		pass


for series in content["content"]:

	currentSeries = Series(series)
	# print(series["metadata"])
	# print("\n")

	# Check if series has field locks
	if skipLock == True:
		if currentSeries.titleLock == True:
			print(currentSeries.name + " - locked... skipped")
			# skippedSeries.append(currentSeries.name)
			continue
		if currentSeries.summaryLock == True:
			print(currentSeries.name + " - locked... skipped")
			# skippedSeries.append(currentSeries.name)
			continue
		if currentSeries.statusLock == True:
			print(currentSeries.name + " - locked... skipped")
			# skippedSeries.append(currentSeries.name)
			continue
		if currentSeries.ageRatingLock == True:
			print(currentSeries.name + " - locked... skipped")
			# skippedSeries.append(currentSeries.name)
			continue
		if currentSeries.tagsLock == True:
			print(currentSeries.name + " - locked... skipped")
			# skippedSeries.append(currentSeries.name)
			continue
		if currentSeries.languageLock == True:
			print(currentSeries.name + " - locked... skipped")
			# skippedSeries.append(currentSeries.name)
			continue
		if currentSeries.publisherLock == True:
			print(currentSeries.name + " - locked... skipped")
			# skippedSeries.append(currentSeries.name)
			continue
		if currentSeries.ageRatingLock == True:
			print(currentSeries.name + " - locked... skipped")
			# skippedSeries.append(currentSeries.name)
			continue

	aniListSeries = mr.lookupSeries(currentSeries) # passes Series class

	if aniListSeries == None:
		skippedSeries.append(currentSeries.name)
		print(currentSeries.name + " skipped")
		continue

	print("\n")


	try:
		kp.patchSeries(session, currentSeries, aniListSeries, ignoreLock) # passes request session Series and anilist class
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



