# ********************
import os, base64


def get_path_parts(path: str):
    if path == None:
        return None

    path = path.strip()

    if path == "":
        return None

    location, tail = os.path.split(p=path)

    items = os.path.splitext(p=tail)

    file_name = items[0]
    file_extension = items[1]

    parts = (location, file_name, file_extension)

    return parts


os.system(command="cls")

source_path = input("File (Convert to Base64): ")

source_path = source_path.strip()
if source_path == "":
    print(f"[!] You did not specify file!")
    quit()

if os.path.exists(path=source_path) == False:
    print(f"[!] File '{source_path}' does not exist!")
    quit()

if os.path.isfile(path=source_path) == False:
    print(f"[!] '{source_path}' is not file!")
    quit()

with open(file=source_path, mode="rb") as file_object:
    file_content = file_object.read()

# کار نمی‌کند urlsafe برای این منظور به خصوص، دستور
# file_content_base64 = base64.urlsafe_b64encode(s=file_content)

file_content_base64 = base64.b64encode(s=file_content)
file_content_base64_string = file_content_base64.decode()

print(file_content_base64_string)

source_path_parts = get_path_parts(path=source_path)
location = source_path_parts[0]
if location != "":
    target_path = f"{location}\\"

target_path = f"{location}{source_path_parts[1]}{source_path_parts[2]}.base64"

with open(file=target_path, mode="wt") as file_object:
    file_object.write(file_content_base64_string)

print("Finished...")
# ********************
