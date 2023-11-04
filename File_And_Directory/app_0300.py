import os

path = "MyFolder"

files_list = []

for (path, folders, files) in os.walk(top=path):
    file_paths = [
        os.path.join(path, file)
        for file in files
    ]

    files_list.extend(file_paths)

for file in files_list:
    print(file)