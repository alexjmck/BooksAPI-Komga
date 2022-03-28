# String sanitization and manipulation functions

import re

# Name parsing and sanitization logic
# has it's own file since I anticipate the logis getting more complex later

def sanitizeName(name): # Try to get clean name without tags
	tempName = name.split(" (")[0] # remove thigs
	tempName2 = tempName.split(" [")[0] # remove thigs
	tempName3  = tempName2.split(" - ")[0]
	tempName4 = tempName3.strip() # removes white space
	return tempName4


# sanitize html tags from string
# used for AniList summary descriptions that contain html tags

# From https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
def sanitizeSummary(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)