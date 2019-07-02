
import os


folder_path = 'C:\\Users\\BS\\Pictures'

os.system('dir {0} /b > output.txt'.format(folder_path))

f = open('output.txt', 'r')
a = f.readline()
print (a)

# DOS command to copy files, create a new folder. list files of directory