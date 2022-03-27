# Push to Komga

def patchSeries(session, komgaSeries, aniListSeries): # pass requests session, Series and anilist class
	





	print(aniListSeries.description)

	pushJSON = '''
{
  "status": "ENDED",
  "statusLock": true,
  "title": "string",
  "titleLock": true,
  "titleSort": "string",
  "titleSortLock": true,
  "summary": "string",
  "summaryLock": true,
  "publisher": "string",
  "publisherLock": true,
  "readingDirectionLock": true,
  "ageRatingLock": true,
  "language": "string",
  "languageLock": true,
  "genresLock": true,
  "tagsLock": true,
  "totalBookCountLock": true,
  "sharingLabelsLock": true,
  "tags": [
    "string"
  ],
  "readingDirection": "LEFT_TO_RIGHT",
  "ageRating": 0,
  "genres": [
    "string"
  ],
  "totalBookCount": 0,
  "sharingLabels": [
    "string"
  ]
}
'''