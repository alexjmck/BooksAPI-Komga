# String sanitization and manipulation functions

import re

# Name parsing and sanitization logic
# has it's own file since I anticipate the logis getting more complex later

def sanitizeName(name): # Try to get clean name without tags
	tempName = name.split(" (")[0] # remove thigs
	tempName = tempName.split(" [")[0] # remove thigs
	tempName  = tempName.split(" - ")[0]
	tempName = tempName.strip() # removes white space
	# tempName = tempName.replace(" ", "+")
	# tempName = tempName.replace(":", "%3A")
	# tempName = tempName.replace("!", "%21")
	# tempName = tempName.replace("?", "%3F")
	# tempName = tempName.replace("=", "%3D")
	# tempName = tempName.replace("&", "%26")
	# tempName = tempName.replace(";", "%3B")
	# tempName = tempName.replace(",", "%2C")
	# tempName = tempName.replace("(", "%28")
	# tempName = tempName.replace(")", "%29")
	# tempName = tempName.replace("'", "%27")
	# tempName = tempName.replace("/", "%2F")
	# tempName = tempName.replace(".", "%2E")
	# tempName = tempName.replace("%", "%25")
	# tempName = tempName.replace("#", "%23")
	# tempName = tempName.replace("$", "%24")
	# tempName = tempName.replace("@", "%40")
	# tempName = tempName.replace("[", "%5B")
	# tempName = tempName.replace("]", "%5D")
	# tempName = tempName.replace("{", "%7B")
	# tempName = tempName.replace("}", "%7D")
	# tempName = tempName.replace("`", "%60")
	# tempName = tempName.replace("<", "%3C")
	# tempName = tempName.replace(">", "%3E")
	# tempName = tempName.replace("|", "%7C")
	# tempName = tempName.replace("~", "%7E")
	# tempName = tempName.replace("^", "%5E")
	# tempName = tempName.replace("_", "%5F")
	# tempName = tempName.replace("-", "%2D")
	# tempName = tempName.replace("+", "%2B")
	return tempName
	# Consider remove "!*" where * is char


# sanitize html tags from string
# used for AniList summary descriptions that contain html tags

# From https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
def sanitizeSummary(text):
	# Verify text is string not null
	if type(text) != str:
		return None

	# Remove html tags from a string
	clean = re.compile('<.*?>')
	return re.sub(clean, '', text)
