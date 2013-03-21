import sys
# sys.path.append("../")
# sys.path.append("../../")
sys.path.append('../')
from PyconBuilder import createImageFromText

def readinwords(infile):
	for line in infile:
		words = line.split(",")
		if len(words) == 5:
			arg = words[0]+'*'+words[1]+'*'+words[2]+'*'+words[3]+'*'+words[4].rstrip()
			createImageFromText(arg,"../images/flash_base.png","../fonts/Arimo-Bold.ttf","*")
	print("ALL FLASH CARDS CREATED")
	
infile = open("../misc/NorwegianVerbs.csv","r")

readinwords(infile)