#
# PYTHON:   version 2.7.13
# AUTHOR:   Annie M Bowman
# PURPOSE:  Tech Academy Python Course DRILL Item #64
#           Write a script that determines whether files in 
#           Folder A have been created or edited within the 
#           last 24 hours and if so, move them to Folder B
#
import shutil
import os
from datetime import datetime
import time

folderA = '/Users/anniebowman/Desktop/FileMovePythonDrill/Folder A/'
folderB = '/Users/anniebowman/Desktop/FileMovePythonDrill/Folder B/'



print "Folder A: {}".format(os.listdir(folderA))
print "Folder B: {}".format(os.listdir(folderB))

for files in os.listdir(folderA): #iterates through contents of Folder A
    fileA = os.path.join(folderA, files) #adds files filename to end of Folder A path
    fileB = os.path.join(folderB, files) #adds files filename to end of Folder B path
    tstamp = os.path.getmtime(fileA) #gets time of most recent modification as a timestamp
    now = time.time() #gets unix time for right now
    last_modified = datetime.fromtimestamp(os.path.getmtime(fileA)).strftime('%I:%M %p %m-%d-%y')
    if tstamp > (now - 86400): #if file was last modified within the last 24hrs:
        print '{} - last modified: {}'.format(files, last_modified)        
        shutil.move(fileA, fileB) #change the directory of each file from Folder A to Folder B

print "Folder A: {}".format(os.listdir(folderA))
print "Folder B: {}".format(os.listdir(folderB))
