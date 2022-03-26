# Meta Search for Komga

This is a supplimentary tool for [https://github.com/gotson/komga](Gotson's Komga Library software)

Retriving metadata for Komga comics using AniList. The motivation behind this project is to match content with metadata in my Komga library that has been aquired from various DRM Free sources like Humble Bundle.

This project was inspired by the [https://github.com/Pfuenzle/AnisearchKomga](AniSearchKomga) script.

The goal is to pull data from aniList's Manga database.

## Name parsing and matching

Ideal folder/series naming should be something like: Name (Year) (Optional Notes), Name (year-year) (optional Notes)

Currently the script asks the user to verify the match before committing to fetch and update the metadata of a series in komga. 

## Further Plans

I may look into saving the data into ComicInfo.xml files. Maybe.

Per volume info may be retirved google books. Will need to define how to recognise volume numbers (ex. toyoureternity_v11.cbz)