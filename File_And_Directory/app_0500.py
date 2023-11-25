"""Application 500"""

import os

os.system(command="cls")

path = input("Path: ")

items = []

for path, folders, files in os.walk(top=path):
    file_paths = [os.path.join(path, file) for file in files]
    items.extend(file_paths)

for file in items:
    print(file)
