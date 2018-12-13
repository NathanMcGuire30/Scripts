import os
import time
import fnmatch
import platform

def copyScreenshots (source):
    #first KSP directory
    #look find number of pictures, and if necicary to do overwrites in destination
    numberofpictures = (len(fnmatch.filter(os.listdir(source), 'screenshot*.png')))
    numberindestination = (len(fnmatch.filter(os.listdir(destination), date + "*.png")))

    #compute range
    minNum = 0
    maxNum = minNum+(numberofpictures)
    if platform.system() == "Windows":
    	
    	for i in range (minNum, maxNum):
        	command = "move " + source + "screenshot" + str(i) + ".png " + destination + date + "_" + str(i + numberindestination) + ".png"
        	os.system(command)
    	os.system("XCOPY /S /Y " + source + "* " + destination)

    elif platform.system() == "Linux":
    	print("Error: no copy scripting written for Linux")

date = time.strftime("%Y-%m-%d")
destination="C:\\Users\\natha\\Pictures\\KSP_Screenshots\\"
copyScreenshots("C:\\Users\\natha\\Desktop\\KSP_win64\\Screenshots\\")
copyScreenshots("C:\\Users\\natha\\Desktop\\KSP_win64_1.4.3\\Screenshots\\")
copyScreenshots("C:\\Users\\natha\\Desktop\\KSP_win64_RSS\\Screenshots\\")
