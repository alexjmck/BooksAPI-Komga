# Class definitions

import sanitizeName as sn


class Series:
  def __init__(self, seriesid, name):
    self.seriesid = seriesid
    self.name = name

  def printName(self):
    print("Series Name: " + self.name)

  def sanitizeName(self):
    return sn.sanitizeName(self.name)

class AniListSeries:
  def __init__(self, id):
    self.id = id