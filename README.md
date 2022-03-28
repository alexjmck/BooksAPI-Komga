# Meta Search for Komga

This is a supplimentary tool for [Gotson's Komga Library software](https://github.com/gotson/komga)

Retriving metadata for Komga comics using AniList. The motivation behind this project is to match content with metadata in my Komga library that has been aquired from various DRM Free sources like Humble Bundle.

This project was inspired by the [AniSearchKomga](https://github.com/Pfuenzle/AnisearchKomga) script.

The goal is to pull data from aniList's Manga database.

## Name parsing and matching

Ideal folder/series naming should be something like: Name (Year) (Optional Notes), Name (year-year) (optional Notes)

Currently the script asks the user to verify the match before committing to fetch and update the metadata of a series in komga. 

## Expected behaviour

You can expect the script to pull all fields from Komga. It will only update *unlocked* fields. When it updates a field it will lock it 
<details>

<summary>Currently it updates fields with the following JSON</summary>

```
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
```

</details>

## Get Started

### Requirements

<ul>
<li>Python 3 (preferably more recent version, My enviroment was python 3.9. I avoided new syntax introduced in python 3.10)</li>
<li>pip - Pip for Python - https://pypi.org/project/pip/ </li>
<li>requests - Requests: HTTP for Humans™ - https://docs.python-requests.org/en/latest/ </li>
</ul>

### Steps

The script is configured by copying the config.template.py into config.py. 

```
# Enter server and credentials here

baseURL="https://example.com" # Include protocol (ie. http:// or https://) and port (if relevant)
user=""
pass=""
```

**Ensure there is no trailing slash in your URL**

Example config:
```
# Enter server and credentials here

baseURL="http://192.168.21.12" # Include protocol (ie. http:// or https://) and port (if relevant)
user="name@email.com"
pass="mySecretPassword"
```

Once saved as `config.py`, using a virtual enviroment. I recommend following a tutorial like this one: [Python Virtual Environments: A Primer
by Real Python](https://realpython.com/python-virtual-environments-a-primer/#using-virtual-environments) (not affiliated)

**Pip** is required. you can install depenancies with
`pip install -r requirements.txt`

The script will be ready to run. Depending on your python installation:
`python getMetadata.py` or `python3 getMetadata.py`



## Further Plans

FuzzyWuzzy fuzzy strings matching.

I may look into saving the data into ComicInfo.xml files. Maybe.

Per volume info may be retirved google books. Will need to define how to recognise volume numbers (ex. toyoureternity_v11.cbz)

Per volume updating is required to assign authorship to series books. 
