# Lookup AniList
import requests, json

from classes import *


query = '''
query($search: String) {
  Page(page:1, perPage:5){
    pageInfo {
      total
      perPage
      currentPage
      lastPage
      hasNextPage
    }
    media(search: $search, type: MANGA, sort: POPULARITY_DESC){
      id
      type
      title {
        english
        romaji
      }
    }
    
  }
}
'''

aniListURL = "https://graphql.anilist.co"

def lookupSeries(series):
	variables = {
	'search':series.name
	}
	response = requests.post(aniListURL, json={'query': query, 'variables': variables})
	print(response.content)