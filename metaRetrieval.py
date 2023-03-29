# Lookup AniList
import requests

from classes import *

# Retrieve list of possible matches query
queryList = '''
query($search: String) {
  Page(page:1, perPage:10){
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
      countryOfOrigin
      format
      genres
      title {
        english
        romaji
        native
      }
      synonyms
    }

  }
}
'''
# Retrieve exact match from id
querySeries = '''
query ($id: Int) {
  Media(id: $id, type: MANGA) {
    id
    idMal
    type
    title {
      romaji
      english
      native
    }
    synonyms
    description
    countryOfOrigin
    isAdult
    status
    volumes
    siteUrl
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

# Start of code for anilist lookup

aniListURL = "https://graphql.anilist.co"

def lookupSeries(series): # pass Series class, returns type AniListSeries

  searchName = series.sanitizeName()# print(searchName)
  variablesList = {'search':searchName}
  seriesOptions = [] # list of possible matches as series IDs
  inputted = None # user input for series selection

  # get paged results 

  try:
    response = requests.post(aniListURL, json={'query': queryList, 'variables': variablesList})
    content = response.json()
    response.raise_for_status()

  except requests.exceptions.HTTPError as errh:
    print(errh)
    print("Skip series")
    return None
  except requests.exceptions.ConnectionError as errc:
    print(errc)
    print("Skip series")
    return None
  except requests.exceptions.Timeout as errt:
    print(errt)
    print("Skip series")
    return None
  except requests.exceptions.RequestException as err:
    print(err)
    print("Skip series")
    return None

  # print series title and locked status
  print("------\n")
  print("For: "+ series.name + "\n")
  series.printLocked()

  if 0 == content["data"]["Page"]["pageInfo"]["total"]: # if no results returned, enter n
    
    print("\nNo series matching search...")
    seriesOptions.append(0) # add 0 to list to prevent empty array error
    inputted = 'n'

  elif 0 != content["data"]["Page"]["pageInfo"]["total"]: # if results returned, print and select
    # Select matching series:
    print("\nSelect the following matching series from AniList:")

    # print(content["data"])
    for resultSeries in content["data"]["Page"]["media"]:
      seriesOptions.append(int(resultSeries["id"]))
      synonymsString = ' \n -------- '.join(resultSeries["synonyms"])
      genresString = ', '.join(resultSeries["genres"])

    # Print Name for selection. Sometimes english returns as None. 
      if resultSeries["title"]["english"] != None:
        print(" \n"+str(len(seriesOptions))+ ") "+ str(resultSeries["id"]) + " -  " +resultSeries["title"]["english"]+ " - " + resultSeries["title"]["romaji"])
      elif resultSeries["title"]["romaji"] != None:
        print(" \n"+str(len(seriesOptions))+ ") "+ str(resultSeries["id"]) + " - " +resultSeries["title"]["romaji"])
      else:
        print("\nNo English or romaji title")
        return None

      if resultSeries["format"] != None and resultSeries["countryOfOrigin"] != None:
        print(" ---- Format: "+resultSeries["format"] + ", "+ resultSeries["countryOfOrigin"])
      elif resultSeries["format"] != None:
        print(" ---- Format: "+resultSeries["format"])

      print(" ---- Synonyms: "+ synonymsString)
      print(" ---- Genres: "+ genresString)

      print("\n------\n")

    inputted = input("\nEnter the correct matching number. If none type 'n': ")

  while True: # validate input is a number or 'n'
    if inputted == 'n':
      # Manual input of anilist code
      aniListID = input("\nEnter custom AniList ID? If no, type 'n': ")
      try:
        seriesOptions[0]= int(aniListID)
        # print(seriesOptions[0])
        inputted = 0
        break
      except:
        print("None matched, series skipped\n")
        return None
    try:
      inputted = int(inputted) - 1
    except:
      inputted = input("Input must be one of the above or 'n': ")
      continue

    if 0 <= inputted and inputted < len(seriesOptions):
      break
    else:
      inputted = input("Input must be one of the above or 'n': ")
      continue

  # Look up series by id on AniList

  variablesSeries = {'id':seriesOptions[inputted]} # sets anilist id for lookup

  try:
    response = requests.post(aniListURL, json={'query': querySeries, 'variables': variablesSeries})
    content = response.json()
    response.raise_for_status()


    # verify retreived json is correct id
    if content["data"]["Media"]["id"] != seriesOptions[inputted]:
      print("AniList did not return correct series by id, skipping...")
      return None
    
    # print series name
    if content["data"]["Media"]["title"]["english"] != None:
      print("\n" + content["data"]["Media"]["title"]["english"] + "\n")
    elif content["data"]["Media"]["title"]["romaji"] != None:
      print("\n" + content["data"]["Media"]["title"]["romaji"] + "\n")
    else:
      print("\nNo English or romaji title")
      return None
    
    print("Series fetched sucessful!")

  except requests.exceptions.HTTPError as errh:
    print(errh)
    print("Skip series")
    return None
  except requests.exceptions.ConnectionError as errc:
    print(errc)
    print("Skip series")
    return None
  except requests.exceptions.Timeout as errt:
    print(errt)
    print("Skip series")
    return None
  except requests.exceptions.RequestException as err:
    print(err)
    print("Skip series")
    return None


  aniListRetrieved = AniListSeries(content) #json returned.

  return aniListRetrieved


# End of code for anilist lookup

# start of code for mangaupdates lookup

# def lookupMangaupdates(series): # pass Series class, returns type MangaupdatesSeries

#   searchName = series.sanitizeName()# print(searchName)

#   # print(searchName)

#   mangaupdatesURL = "https://www.mangaupdates.com/series.html?search=" + searchName

#   try:
#     response = requests.get(mangaupdatesURL)
#     content = response.text
#     response.raise_for_status()

#   except requests.exceptions.HTTPError as errh:
#     print(errh)
#     print("Skip series")
#     return None
#   except requests.exceptions.ConnectionError as errc:


# return mangaupdatesRetrieved
