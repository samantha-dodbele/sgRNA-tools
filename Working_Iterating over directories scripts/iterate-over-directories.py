import os

# How to iterate through files and print out the names of the files
directory = 'C:/Users/Samantha/Box Sync/Wilusz Lab/Test'

for root, subdirectories, files in os.walk(directory):
    # print the subdirectory path
    for subdirectory in subdirectories:
        print(os.path.join(root, subdirectory))
       
    # prints the file path and the files within subdirectories
    for file in files:
        print(os.path.join(root, file))

    # prints just the name of the subdirectory
    for subdirectory in subdirectories:
        print(subdirectory)