# A script to retrieve metadata from AniList for Komga.

import requests, sys

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
print(" ")
numSeries = None
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

orderRetrieved = 0
isTrue = True
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

ignoreLock = None
while True:
	try:
		ignoreLock = ignoreLockDict[input("Override field locks? (y/n): ")]
		break
	except:
		pass



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



