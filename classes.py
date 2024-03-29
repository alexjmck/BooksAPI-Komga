# Class definitions

import sanitizeString as ss

# Komga Series Class
class Series:
  def __init__(self, series): # passes json of series

    self.seriesid = series["id"]
    self.name = series["name"]

    self.metadataJSON = series["metadata"]
    # Patchable metadata fields
    self.status = self.metadataJSON["status"]
    self.statusLock = self.metadataJSON["statusLock"]

    self.title = self.metadataJSON["title"]
    self.titleLock = self.metadataJSON["titleLock"]

    self.titleSort = self.metadataJSON["titleSort"]
    self.titleSortLock = self.metadataJSON["titleSortLock"]

    self.summary = self.metadataJSON["summary"]
    self.summaryLock = self.metadataJSON["summaryLock"]

    self.publisher = self.metadataJSON["publisher"]
    self.publisherLock = self.metadataJSON["publisherLock"]

    self.readingDirection = self.metadataJSON["readingDirection"]
    self.readingDirectionLock = self.metadataJSON["readingDirectionLock"]

    self.ageRating = self.metadataJSON["ageRating"]
    self.ageRatingLock = self.metadataJSON["ageRatingLock"]

    self.language = self.metadataJSON["language"]
    self.languageLock = self.metadataJSON["languageLock"]

    self.genres = self.metadataJSON["genres"]
    self.genresLock = self.metadataJSON["genresLock"]

    self.tags = self.metadataJSON["tags"]
    self.tagsLock = self.metadataJSON["tagsLock"]

    self.totalBookCount = self.metadataJSON["totalBookCount"]
    self.totalBookCountLock = self.metadataJSON["totalBookCountLock"]

    self.sharingLabels = self.metadataJSON["sharingLabels"]
    self.sharingLabelsLock = self.metadataJSON["sharingLabelsLock"]

  def printName(self):
    print("Series Name: " + self.name)
  
  def printLocked(self):
    print("Summary Locked?: " + str(self.summaryLock))
    print("Title Locked?: " + str(self.titleLock))
    print("Title Sort Locked?: " + str(self.titleSortLock))
    print("Status Locked?: " + str(self.statusLock))
    print("Publisher Locked?: " + str(self.publisherLock))
    print("Reading Direction Locked?: " + str(self.readingDirectionLock))
    print("Age Rating Locked?: " + str(self.ageRatingLock))
    print("Language Locked?: " + str(self.languageLock))
    print("Genres Locked?: " + str(self.genresLock))
    print("Tags Locked?: " + str(self.tagsLock))
    print("Total Book Count Locked?: " + str(self.totalBookCountLock))
    print("Sharing Labels Locked?: " + str(self.sharingLabelsLock))


  def sanitizeName(self):
    return ss.sanitizeName(self.name)



# AniList Series class
class AniListSeries:

  def __init__(self, content):# Accepts response.json() content from a request and parses the data into the object
    # TODO implement id check
    self.media = content["data"]["Media"]

    self.id = self.media["id"] 
    self.type = self.media["type"]
    self.titleRomaji = self.media["title"]["romaji"] # Titles
    self.titleEnglish = self.media["title"]["english"]
    self.titleNative = self.media["title"]["native"]
    self.synonyms = self.media["synonyms"]
    self.description = ss.sanitizeSummary(self.media["description"])
    self.countryOfOrigin = self.media["countryOfOrigin"]
    self.isAdult = self.media["isAdult"]
    self.status = self.media["status"]
    self.volumes = self.media["volumes"]
    self.genres = self.media["genres"]
    self.tags = self.media["tags"]
    self.staff = self.media["staff"]

# class AniListStaff:
#   def __init__(self, staff):
#   edges {
#     role
#     node {
#       id
#     }
#   }
#   nodes {
#     id
#     name {
#       first
#       middle
#       last
#       full
#       native
#       userPreferred
#     }
#   }


