# Push to Komga

import requests, json

from config import *

def patchSeries(session, komgaSeries, aniListSeries, ignoreLock): # pass requests session, Series and anilist class

  # Assign Anilist data to komga object
  # Any locked fields will be ignored
  # Edited fields will be locked

  # ---- Status Anilist -> Komga
  statusDict = {
    'FINISHED': 'ENDED',
    'RELEASING': 'ONGOING',
    'CANCELLED': 'ABANDONED',
    'HIATUS': 'HIATUS'
  }

  readingDirectionDict = {
    'JP': "RIGHT_TO_LEFT",
    'KR': " WEBTOON",
    'CN': "RIGHT_TO_LEFT",
    'TW': "RIGHT_TO_LEFT"
  }

  if ignoreLock == True:
    # Resets locks locally to False
    komgaSeries.statusLock = False
    komgaSeries.titleLock = False
    komgaSeries.titleSortLock = False
    komgaSeries.summaryLock = False
    komgaSeries.readingDirectionLock = False
    komgaSeries.ageRatingLock = False
    komgaSeries.languageLock = False
    komgaSeries.genresLock = False
    komgaSeries.totalBookCountLock = False
    komgaSeries.tagsLock = False


  # NOT_YET_RELEASED -> skip
  if aniListSeries.status != "NOT_YET_RELEASED" and komgaSeries.statusLock == False:
    komgaSeries.status = statusDict[aniListSeries.status]
    komgaSeries.statusLock = True

  # ---- Title saves English - Romanji ## note currently native only names are not retrieved so case doesn't account for that here.
  if komgaSeries.titleLock == False:
    if aniListSeries.titleEnglish == None:
      komgaSeries.title = aniListSeries.titleRomaji
    else:
      komgaSeries.title = aniListSeries.titleEnglish + " - " + aniListSeries.titleRomaji

    komgaSeries.titleLock = True # Lock title

  # ---- TitleSort duplicates title
  if komgaSeries.titleSortLock == False:
    komgaSeries.titleSort = komgaSeries.title
    komgaSeries.titleSortLock = True

  # ---- Summary
  if komgaSeries.summaryLock == False:
    komgaSeries.summary = aniListSeries.description
    komgaSeries.summaryLock = True

  # ---- reading direction
  if komgaSeries.readingDirectionLock == False:
    komgaSeries.readingDirection = readingDirectionDict.get(aniListSeries.countryOfOrigin) # return None if country missmatch

    if komgaSeries.readingDirection != None:
      komgaSeries.readingDirectionLock = True

  # ---- Age rating
  if komgaSeries.ageRatingLock == False and aniListSeries.isAdult == True:
    komgaSeries.ageRating = "18"
    komgaSeries.ageRatingLock = True

  # ---- Language == English
  if komgaSeries.languageLock == False:
    komgaSeries.language = "en-US"
    komgaSeries.languageLock = True

  # ---- Genres
  if komgaSeries.genresLock == False:
    komgaSeries.genres = aniListSeries.genres
    komgaSeries.genresLock = True

  # ---- Total Book count ** ONly updated by volume if series finished on anilist.
  if komgaSeries.totalBookCountLock == False and aniListSeries.status == "FINISHED":
    # also verify omnibus isn't in komga title
    if "mnibus" not in komgaSeries.name: # 'mnibus' short for 'omnibus' but cap and non
      komgaSeries.totalBookCount = aniListSeries.volumes
      komgaSeries.totalBookCountLock = True

  # ---- Tags * requires certain parsing, currently does not filter out isSpoiler or isAdult
  if komgaSeries.tagsLock == False:
    tagsParsed = []
    for tag in aniListSeries.tags:
      tagsParsed.append(tag["name"])
    komgaSeries.tags = tagsParsed
    komgaSeries.tagsLock = True

  # print("verify passed " + aniListSeries.titleEnglish)

  # dictionary for bool to turn lower case for Komga
  boolDict = {
    True: 'true',
    False: 'false'
  }

  # input variables to json string
  pushJSONDict = {
  "status": komgaSeries.status,
  "statusLock": boolDict[komgaSeries.statusLock],
  "title": komgaSeries.title,
  "titleLock": boolDict[komgaSeries.titleLock],
  "titleSort": komgaSeries.titleSort,
  "titleSortLock": boolDict[komgaSeries.titleSortLock],
  "summary": komgaSeries.summary,
  "summaryLock": boolDict[komgaSeries.summaryLock],
  "publisher": komgaSeries.publisher,
  "publisherLock": boolDict[komgaSeries.publisherLock],
  "readingDirectionLock": boolDict[komgaSeries.readingDirectionLock],
  "ageRatingLock": boolDict[komgaSeries.ageRatingLock],
  "language": komgaSeries.language,
  "languageLock": boolDict[komgaSeries.languageLock],
  "genresLock": boolDict[komgaSeries.genresLock],
  "tagsLock": boolDict[komgaSeries.tagsLock],
  "totalBookCountLock": boolDict[komgaSeries.totalBookCountLock],
  "tags": komgaSeries.tags,
  "readingDirection": komgaSeries.readingDirection,
  "ageRating": komgaSeries.ageRating,
  "genres": komgaSeries.genres,
  "totalBookCount": komgaSeries.totalBookCount,
}


  # print(pushJSONDict)

  # Patch request
  try:
    responsePatch = session.patch(baseURL + "/api/v1/series/" + komgaSeries.seriesid + "/metadata", data=json.dumps(pushJSONDict))

    # verify if updated right
    if responsePatch.json() != None:
      print("did not return 204")
      print(responsePatch.json())

    responsePatch.raise_for_status()

    print("Series updated sucessfully!\n")

  except requests.exceptions.HTTPError as errh:
    print(errh)
    print("Skip series, update failed errh")
    print(responsePatch.json())
    raise errh
  except requests.exceptions.ConnectionError as errc:
    print(errc)
    print("Skip series, update failed errc")
    raise errc
  except requests.exceptions.Timeout as errt:
    print(errt)
    print("Skip series, update failed errt")
    raise errt
  except requests.exceptions.RequestException as err:
    if responsePatch.status_code == 204: # 204 is expected
      print("Series updated sucessfully!\n")
      return None
    print(err)
    print("Skip series, update failed err")
    raise err

  print("Updated series "+ komgaSeries.title)

