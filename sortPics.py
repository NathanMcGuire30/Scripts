import os
import time
import fnmatch
import sys


date = time.strftime("%Y-%m-%d_%H.%M.%S")


destination=str(sys.argv[1])				#Need to define destination in program call 
source = str(sys.argv[2])					#Where to put files

files = os.listdir(source)
jpgs = []
pngs = []

for i in range (0, len(files)):
		if ".jpg" in files[i]:
			name = files[i].split(".")
			print(source + files[i])
			os.rename(source + files[i], destination + name[0] + "+" + date + ".jpg")

		if ".png" in files[i]:
			name = files[i].split(".")
			print(source + files[i])
			os.rename(source + files[i], destination + name[0] + "+" + date + ".png")