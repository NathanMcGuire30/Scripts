import os
import time
import fnmatch
import platform
import sys



date = time.strftime("%Y-%m-%d")

source = str(sys.argv[1])
destination=str(sys.argv[2])

#first KSP directory
#look find number of pictures, and if necesscary to do overwrites in destination
numberofpictures = (len(fnmatch.filter(os.listdir(source), 'screenshot*.png')))
numberindestination = (len(fnmatch.filter(os.listdir(destination), date + "*.png")))

for i in range (0, numberofpictures):
	print(source + "screenshot" + str(i) + ".png")
	os.rename(source + "screenshot" + str(i) + ".png ", destination + date + "_" + str(i + numberindestination) + ".png")
    
#os.system("XCOPY /S /Y " + source + "* " + destination)


