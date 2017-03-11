#
# PYTHON:   version 2.7.13
# AUTHOR:   Annie M Bowman
# PURPOSE:  Tech Academy Python Course DRILL Item #63
#           Write a program that moves 4 .txt files from 
#           Folder A to Folder B and print transfer path 
#           of each moved file to the shell.
#
import shutil
import os

folderA = '/Users/anniebowman/Desktop/FileMovePythonDrill/Folder A/'
folderB = '/Users/anniebowman/Desktop/FileMovePythonDrill/Folder B/'

print "Folder A: {}".format(os.listdir(folderA))
print "Folder B: {}".format(os.listdir(folderB))

for files in os.listdir(folderA): #iterates through contents of Folder A
    fileA = os.path.join(folderA, files) #adds files filename to end of pathA
    fileB = os.path.join(folderB, files) #adds files filename to end of pathB
    print 'Moving: {} from: {}'.format(files, folderA)
    shutil.move(fileA, fileB) #changes directory of each file from Folder A to Folder B
    print 'To: {}'.format(folderB)
    print ''


print "Folder A: {}".format(os.listdir(folderA))
print "Folder B: {}".format(os.listdir(folderB))
