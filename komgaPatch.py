# Push to Komga

def patchSeries(session, komgaSeries, aniListSeries): # pass requests session, Series and anilist class

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
  if komgaSeries.readingDirectionLock == False and aniListSeries.type == "MANGA":
    komgaSeries.readingDirection == "RIGHT_TO_LEFT"
    komgaSeries.readingDirectionLock == True

  # ---- Age rating
  if komgaSeries.ageRatingLock == False and aniListSeries.isAdult == True:
    komgaSeries.ageRating = "18"
    komgaSeries.ageRatingLock = True

  # ---- Language == English
  if komgaSeries.languageLock == False:
    komgaSeries.language = "English"
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

  print("verify passed " + aniListSeries.titleEnglish)

  # passing these lists into a string
  patchTags = "[\n\""+'\"\n\"'.join(komgaSeries.tags)+"\"\n]"
  patchGenres = "[\n\""+'\"\n\"'.join(komgaSeries.genres)+"\"\n]"

  # input variables to json string
  pushJSON = '''
{
  "status": "%s",
  "statusLock": %r,
  "title": "%s",
  "titleLock": %r,
  "titleSort": "%s",
  "titleSortLock": %r,
  "summary": "%s",
  "summaryLock": %r,
  "publisher": "%s",
  "publisherLock": %r,
  "readingDirectionLock": %r,
  "ageRatingLock": %r,
  "language": "%s",
  "languageLock": %r,
  "genresLock": %r,
  "tagsLock": %s,
  "totalBookCountLock": %r,
  "tags": %s,
  "readingDirection": "%s",
  "ageRating": %s,
  "genres": %s,
  "totalBookCount": %s,
}
''' % (komgaSeries.status,
  komgaSeries.statusLock, 
  komgaSeries.title, 
  komgaSeries.titleLock,
  komgaSeries.titleSort,
  komgaSeries.titleSortLock,
  komgaSeries.summary,
  komgaSeries.summaryLock,
  komgaSeries.publisher,
  komgaSeries.publisherLock,
  komgaSeries.readingDirectionLock,
  komgaSeries.ageRatingLock,
  komgaSeries.language,
  komgaSeries.languageLock,
  komgaSeries.genresLock,
  komgaSeries.tagsLock,
  komgaSeries.totalBookCountLock,
  patchTags,
  komgaSeries.readingDirection,
  komgaSeries.ageRating,
  patchGenres,
  komgaSeries.totalBookCount,
  )

  print(pushJSON)


# 	pushJSON = '''
# {
#   "status": "ENDED",
#   "statusLock": true,
#   "title": "string",
#   "titleLock": true,
#   "titleSort": "string",
#   "titleSortLock": true,
#   "summary": "string",
#   "summaryLock": true,
#   "publisher": "string",
#   "publisherLock": true,
#   "readingDirectionLock": true,
#   "ageRatingLock": true,
#   "language": "string",
#   "languageLock": true,
#   "genresLock": true,
#   "tagsLock": true,
#   "totalBookCountLock": true,
#   "sharingLabelsLock": true,
#   "tags": [
#     "string"
#   ],
#   "readingDirection": "LEFT_TO_RIGHT",
#   "ageRating": 0,
#   "genres": [
#     "string"
#   ],
#   "totalBookCount": 0,
#   "sharingLabels": [
#     "string"
#   ]
# }
# '''