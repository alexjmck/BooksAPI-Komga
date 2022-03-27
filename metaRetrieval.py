# Lookup AniList
import requests, json

from classes import *

# Retrieve list of possible matches query
queryList = '''
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
# Retrieve exact match from id
querySeries = '''
query ($id: Int) {
  Media(id: $id, type: MANGA) {
    id
    type
    title {
      romaji
      english
      native
    }
    description
    isAdult
    status
    volumes
    genres
    tags {
      id
      name
      isMediaSpoiler
      isAdult
    }
    staff {
      edges {
        role
        node {
          id
        }
      }
      nodes {
        id
        name {
          first
          middle
          last
          full
          native
          userPreferred
        }
      }
    }
  }
}
'''

# Start of code 

aniListURL = "https://graphql.anilist.co"

def lookupSeries(series):

  searchName = series.sanitizeName()# print(searchName)

  variablesList = {'search':searchName}

  # print(series.sanitizeName())

  # get paged results 

  try:
    response = requests.post(aniListURL, json={'query': queryList, 'variables': variablesList})
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


  variablesSeries = {'id':seriesOptions[inputted]} # sets anilist id for lookup


  try:
    response = requests.post(aniListURL, json={'query': querySeries, 'variables': variablesSeries})
    content = response.json()
    response.raise_for_status()
    print("Series fetched sucessful!\n")

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
  print(content)








