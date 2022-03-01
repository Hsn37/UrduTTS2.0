import re
from sys import argv

newMappings = {

	"TT":"T",
	"TT_H":"T_H",
	"DD":"D",
	"NG":"N_G",
	"SH":"S_H",
	"ZZ":"Z_Z",
	"7":"G_G",
	"RR":"R_R",
	"RR_H":"R_R_H",
	"T_SH":"T_S",
	"T_SH_H":"T_S_H",
	"D_ZZ":"D_Z",
	"D_ZZ_H":"D_Z_H",
	"UU":"U_U",
	"UUN": "U_U_N",
	"OO": "O_O",
	"ON":"O_N",
	"AA":"A_A",
	"AAN":"A_A_N",
	"II":"I_I",
	"IIN":"I_I_N",
	"AE":"A_E",
	"AEN":"A_E_N",
	"AY":"A_Y",
	"AYN":"A_Y_N"
}


def mapToNewPhoneme(line):
	line = re.sub("##", " ## ", line)
	k = line.split()
	newLine = []
	for w in k:
		if w != "":
			try:
				newLine.append(newMappings[w])
			except:
				newLine.append(w)

	return " ".join(newLine)


def cleanString(x):
	x = re.sub("<s>|</s>", "", x)
	x = mapToNewPhoneme(x)
	y = x.split("##")
	z = ["{" + w.strip() + "}" for w in y if w.strip() != ""]

	return " ".join(z)


def preprocessTrainData(filename):
	# Read the dataset
	f = open(filename, "r")
	lines = f.readlines()[2:]
	f.close()


	# clean the strings
	newLines = []
	l = 1
	for x in lines:
		newStr = cleanString(x)
		newLines.append("c" + str(l) + "|" + newStr + "|" + newStr + "\n")
		l += 1


	# writeout the strings to metadata.csv
	f = open("metadata.csv", "w")
	for l in newLines:
		f.write(l)
	f.close()


if __name__ == "__main__":
	try:
		preprocessTrainData(argv[1])
		print("SUCCESS: metadata.csv created.")
	except:
		print("ERROR: Pass the path of the transcription file as the first parameter.")