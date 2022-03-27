# Class definitions

import sanitizeName as sn

# Komga Series Class
class Series:
  def __init__(self, seriesid, name):
    self.seriesid = seriesid
    self.name = name

  def printName(self):
    print("Series Name: " + self.name)

  def sanitizeName(self):
    return sn.sanitizeName(self.name)


# AniList Series class
class AniListSeries:

  def __init__(self, id, content):# Accepts response.json() content from a request and parses the data into the object
    # TODO implement id check
    self.media = content["data"]["Media"]

    self.id = self.media["id"] 
    self.type = self.media["type"]
    self.titleRomaji = self.media["title"]["romaji"] # Titles
    self.titleEnglish = self.media["title"]["english"]
    self.titleNative = self.media["title"]["native"]
    self.description = self.media["description"]
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