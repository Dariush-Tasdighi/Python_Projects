"""Application 400"""

import os

os.system(command="cls")

PATH = "MyFolder"

files_list = []

for path, folders, files in os.walk(top=PATH):
    file_paths = [os.path.join(path, file) for file in files]

    files_list.extend(file_paths)

for file in files_list:
    print(file)
