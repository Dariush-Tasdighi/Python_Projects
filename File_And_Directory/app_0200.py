"""Application 200"""

import os

os.system(command="cls")

print("OS Name:", os.name)
print("Current Working Directory:", os.getcwd())

print()

PATH = "C:\\Windows"
print(f"{PATH} exists:", os.path.exists(path=PATH))

PATH = "C:\\Windows\\notepad.exe"
print(f"{PATH} exists:", os.path.exists(path=PATH))

print()

PATH = "C:\\some_folder"
print(f"{PATH} exists:", os.path.exists(path=PATH))

PATH = "C:\\Windows\\some_file.exe"
print(f"{PATH} exists:", os.path.exists(path=PATH))

print()

# معمولا ابتدا تست می‌کنیم که مسیر اعلام شده وجود دارد یا خیر
# و سپس بررسی می‌کنیم که این مسیر مربوط به فایل است و یا پوشه؟

PATH = "C:\\Windows"
if os.path.exists(path=PATH):
    print(f"{PATH} is File:", os.path.isfile(path=PATH))
    print(f"{PATH} is Directory:", os.path.isdir(s=PATH))

print()

PATH = "C:\\Windows\\notepad.exe"
if os.path.exists(path=PATH):
    print(f"{PATH} is File:", os.path.isfile(path=PATH))
    print(f"{PATH} is Directory:", os.path.isdir(s=PATH))

print()
