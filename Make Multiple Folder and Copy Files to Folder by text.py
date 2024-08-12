import os
from pathlib import Path
import shutil

# change directory
path = "./"

Folder01 = input("Name of first folder > ")
Folder02 = input("Name of second folder > ")
Folder03 = input("Name of third folder > ")
Folder04 = input("Name of forth folder > ")

# crete a list contain multiple folder
list = [Folder01, Folder02, Folder03, Folder04]

# create folder base on list
for items in list:
    os.mkdir(items)


# declare variables
folder01_path = os.path.join(path, Folder01)
folder02_path = os.path.join(path, Folder02)
folder03_path = os.path.join(path, Folder03)
folder04_path = os.path.join(path, Folder04)

print("Move file based on text")
filenameconsist01 = input(f"Text filter for {Folder01} folder > ")
filenameconsist02 = input(f"Text filter for {Folder02} folder > ")
filenameconsist03 = input(f"Text filter for {Folder03} folder > ")
filenameconsist04 = input(f"Text filter for {Folder04} folder > ")


# # if file name contain "A" then copy the file from X to Y
# for file in os.listdir():
#     if "Anime" in file:
#         shutil.copy2(file, folder01_path)
#     if "Beautiful" in file:
#         shutil.copy2(file, folder02_path)
#     if "Drama" in file:
#         shutil.copy2(file, folder03_path)
#     if "Good" in file:
#         shutil.copy2(file, folder04_path)

# if file name contain "A" then copy the file from X to Y
for file in os.listdir():
    if filenameconsist01 in file:
        shutil.copy2(file, folder01_path)
    if filenameconsist02 in file:
        shutil.copy2(file, folder02_path)
    if filenameconsist03 in file:
        shutil.copy2(file, folder03_path)
    if filenameconsist04 in file:
        shutil.copy2(file, folder04_path)
