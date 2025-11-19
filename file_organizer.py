"""
1. Create a new Python script named file_organizer.py.
2. Use the os.mkdir() function to create a new directory named MyFiles.
3. Inside MyFiles, create three subdirectories named Docs, Images, 
and Videos using the same mkdir() function.
"""

#create a directory
import os
os.mkdir('Myfiles')

def main():
    # create MyFiles folder + three subdirectories
    os.mkdir('MyFiles/Docs')
    os.mkdir('MyFiles/Images')
    os.mkdir('MyFiles/Videos')

main()