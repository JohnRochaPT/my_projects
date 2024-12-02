"""
Clean Git-bash history file 

The file records every command you enter even if you enter it 100 times.  Requirements:
    Get the path for the file
    Get the file name
    Read the entire file and store each line in a list
    Walk through the list to create a new one for lines that are unique.
    Add mandatory commands:
    myNewList.append('exit')
    myNewList.append('ls -l')
    myNewList.append('python Exercise#.#.py')
    myNewList.append('winpty  /C/Users/jarocha/Anaconda3/python.exe')
    myNewList.append('cd D:Dropbox/Learn/YTb/FCCP4B/')
    myNewList.append('cd D:Dropbox/Learn/eCornell/CIS552')
    myNewList.append('cd D:Dropbox/Learn/edX/CS50P')
    myNewList.append('conda activate CIS552')
    myNewList.append('conda activate train1')
    myNewList.append('conda activate CS50P')
    myNewList.append('python DelHistory.py')
    myNewList.append('history -c')
"""
__author__ = "John Rocha"
__date__ = "2024/09/04"

import codecs

# Get the file location.  By default use "C:\Users\jarocha" if nothing entered.
# Get the file name.  By default use ".bash_history"
filePath = 'C:\\Users\\jarocha\\'
# print(filePath)
fileName = '.bash_history'
# print('The complete file name and path is: \n')
completeName = filePath + fileName
# print(completeName)

# create a new list and add the minimum lines
myNewList = list()
# myNewList.append('conda create --name')
# myNewList.append('conda install python')
myNewList.append('exit')
myNewList.append('ls -l')
myNewList.append('python Exercise#.#.py')
myNewList.append('winpty  /C/Users/jarocha/Anaconda3/python.exe')
myNewList.append('cd D:Dropbox/Learn/YTb/FCCP4B/')
myNewList.append('cd D:Dropbox/Learn/eCornell/CIS552')
myNewList.append('cd D:Dropbox/Learn/edX/CS50P')
myNewList.append('conda activate CIS552')
myNewList.append('conda activate train1')
myNewList.append('conda activate CS50P')
myNewList.append('python DelHistory.py')
myNewList.append('history -c')

# print(myNewList)
# Now open the file
try:
    myFile = codecs.open(completeName, 'w', "utf-8")
#    print('File successfully opened for read')
except:
    print('Unable to open the file')
    quit()

myFile.seek(0)
myFile.truncate()

# Now write the desired commands
for line in myNewList:
    if line != 'Exit':
        myFile.write(line + '\n')
    else:
        myFile.write(line)

# Now close the file
print('All clear now.  Ready to close')
myFile.close()
