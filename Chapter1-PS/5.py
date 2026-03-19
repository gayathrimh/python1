import os
#specify the dir path
path="/"
#gets list of files and folders using os module
contents=os.listdir(path)
#print directory
print("directory contents")
for item in contents:
    print(item)