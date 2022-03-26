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

  searchName = series.sanitizeName()# print(searchName)

  variables = {'search':searchName}

  # print(series.sanitizeName())

  # get paged results 

  try:
    response = requests.post(aniListURL, json={'query': query, 'variables': variables})
    content = response.json()
    response.raise_for_status()
    print("Login to Komga sucessful!\n")

  except requests.exceptions.HTTPError as errh:
    print(errh)
    print("Skip series")
    return
  except requests.exceptions.ConnectionError as errc:
    print(errc)
    print("Skip series")
    return
  except requests.exceptions.Timeout as errt:
    print(errt)
    print("Skip series")
    return
  except requests.exceptions.RequestException as err:
    print(err)
    print("Skip series")
    return


  # Select matching series:
  print("For "+ series.name)
  print("Select the following matching series from AniList:\n")

  seriesOptions = []
  # print(content["data"])
  for resultSeries in content["data"]["Page"]["media"]:
    seriesOptions.append(int(resultSeries["id"]))

  # Print Name for seleection. SOmetimes english returns as null. 
    if resultSeries["title"]["english"] != None:
      print(str(len(seriesOptions))+ ") "+ str(resultSeries["id"]) + " -  " +resultSeries["title"]["english"]+ " - " + resultSeries["title"]["romaji"])
    elif resultSeries["title"]["romaji"] != None:
      print(str(len(seriesOptions))+ ") "+ str(resultSeries["id"]) + " - " +resultSeries["title"]["romaji"])
    else:
      return

  print("\nNone of the above, skip series lookup (n)\n")

  inputted = input("Enter the correct matching number. If none type 'n': ")

  if inputted == 'n':
    print("None matched, series skipped")
    return

  inputted = int(inputted) - 1 
  print(seriesOptions[inputted])
  print(content["data"]["Page"]["media"][inputted])

  type(inputted)

  # Look up series by id on AniList









