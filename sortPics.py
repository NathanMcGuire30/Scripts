import os
import time
import fnmatch


date = time.strftime("%Y-%m-%d_%H.%M.%S")
destination="C:\\Users\\natha\\Pictures\\misc\\"

print(date)

os.system("ren \"C:\\Users\\natha\\Downloads\\*.jpg\" \"*.\"")
os.system("ren \"C:\\Users\\natha\\Downloads\\*.\" \"*_\"" + date)
os.system("ren \"C:\\Users\\natha\\Downloads\\*_" + date + "\" \"*_" + date + ".jpg\"")

os.system("move C:\\Users\\natha\\Downloads\\*.jpg C:\\Users\\natha\\Pictures\\misc\\")

os.system("ren \"C:\\Users\\natha\\Downloads\\*.png\" \"*.\"")
os.system("ren \"C:\\Users\\natha\\Downloads\\*.\" \"*_\"" + date)
os.system("ren \"C:\\Users\\natha\\Downloads\\*_" + date + "\" \"*_" + date + ".png\"")

os.system("move C:\\Users\\natha\\Downloads\\*.png C:\\Users\\natha\\Pictures\\misc\\")