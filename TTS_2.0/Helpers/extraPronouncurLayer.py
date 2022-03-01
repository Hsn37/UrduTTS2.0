import re 


#############################################
####### HELPER
# For the pronouncUR. Converts its output into the format that tacotron expects. Simply call this function on each string.

def transformText(text):
	parts = text.split()
	newString = ""
	for q in parts:
		x = re.sub(r"([A-Z]_[A-Z]_[A-Z]|[A-Z]_[A-Z])", r" \1 ", q)
		y = x.split()
		z = ["".join([p + " " for p in w]).strip() if "_" not in w else w for w in y]
		newString += "{" + " ".join(z) + "}" + " "

	return newString.strip()
