import os
import shutil

sourceFolder = input("Please enter the Source Location: ")
DestinationFolder = input("Please enter the Destination Foldler location: ")
extension = input("Now enter the file type extension: ")

for folder, subfolders, filenames in os.walk(sourceFolder):
    for filename in filenames:
        print(filename)
        if filename.endswith('{}'.format(extension)):
            shutil.copy(os.path.join(folder, filename), DestinationFolder)
