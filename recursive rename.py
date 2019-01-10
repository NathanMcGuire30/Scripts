import os
import time
import fnmatch
import platform
import sys




    


def renameFiles(filepath):
	filepath += "\\"
	filelist = fnmatch.filter(os.listdir(filepath), "*.S*")
	numberindestination = len(filelist)

	print(numberindestination)
	

	for i in range (0, numberindestination):
		filename = filelist[i].split(".S")[0]
		filetype = ".S" + filelist[i].split(".S")[1]
		#print(filetype)
		print(filepath + filename + "_common" + filetype)
		os.rename(filepath + filelist[i], filepath + "\\" + filename + "_common" + filetype)

	#print(source + "screenshot" + str(i) + ".png")
	

def directoryList(filepath):
	print(os.listdir(d))


rootTarget = str(sys.argv[1])
#renameFiles(rootTarget)
directoryList(rootTarget)