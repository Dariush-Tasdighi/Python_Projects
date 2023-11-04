import os

print("OS Name:", os.name)
print("Current Working Directory:", os.getcwd())

print()

path = "C:\\Windows"
print(f"{path} exists:", os.path.exists(path=path))

path_name = "C:\\Windows\\notepad.exe"
print(f"{path_name} exists:", os.path.exists(path=path_name))

print()

path = "C:\\alaki"
print(f"{path} exists:", os.path.exists(path=path))

path_name = "C:\\Windows\\alaki.exe"
print(f"{path_name} exists:", os.path.exists(path=path_name))

print()

path = "C:\\Windows"
if os.path.exists(path=path):
    print(f"{path} is File:", os.path.isfile(path=path))
    print(f"{path} is Directory:", os.path.isdir(s=path))

path_name = "C:\\Windows\\notepad.exe"
if os.path.exists(path=path_name):
    print(f"{path_name} is File:", os.path.isfile(path=path_name))
    print(f"{path_name} is Directory:", os.path.isdir(s=path_name))

print()

path = "C:\\Windows"
if os.path.exists(path=path):
    print(f"{path} is File:", os.path.isfile(path=path))
    print(f"{path} is Directory:", os.path.isdir(s=path))

path_name = "C:\\Windows\\notepad.exe"
if os.path.exists(path=path_name):
    print(f"{path_name} is File:", os.path.isfile(path=path_name))
    print(f"{path_name} is Directory:", os.path.isdir(s=path_name))

print()
