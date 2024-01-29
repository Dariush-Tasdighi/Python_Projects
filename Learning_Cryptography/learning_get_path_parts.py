import os

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

path = None
parts = get_path_parts(path=path)
if parts != None:
    print(f"[!] Path Parsing Error! - '{path}'")

path = ""
parts = get_path_parts(path=path)
if parts != None:
    print(f"[!] Path Parsing Error! - '{path}'")

path = "     "
parts = get_path_parts(path=path)
if parts != None:
    print(f"[!] Path Parsing Error! - '{path}'")

path = "Alaki"
parts = get_path_parts(path=path)
if ("", "Alaki", "") != parts:
    print(f"[!] Path Parsing Error! - '{path}'")

path = "Alaki.txt"
parts = get_path_parts(path=path)
if ("", "Alaki", ".txt") != parts:
    print(f"[!] Path Parsing Error! - '{path}'")

path = "Alaki.Dolaki.txt"
parts = get_path_parts(path=path)
if ("", "Alaki.Dolaki", ".txt") != parts:
    print(f"[!] Path Parsing Error! - '{path}'")

path = "     Alaki.Dolaki.txt     "
parts = get_path_parts(path=path)
if ("", "Alaki.Dolaki", ".txt") != parts:
    print(f"[!] Path Parsing Error! - '{path}'")

# In Windows

path = "C:\\A\\"
parts = get_path_parts(path=path)
if ("C:\\A", "", "") != parts:
    print(f"[!] Path Parsing Error! - '{path}'")

path = "C:\\A\\Alaki.Dolaki.txt"
parts = get_path_parts(path=path)
if ("C:\\A", "Alaki.Dolaki", ".txt") != parts:
    print(f"[!] Path Parsing Error! - '{path}'")

# In Linux / Mac

path = "/A/"
parts = get_path_parts(path=path)
if ("/A", "", "") != parts:
    print(f"[!] Path Parsing Error! - '{path}'")

path = "/A/Alaki.Dolaki.txt"
parts = get_path_parts(path=path)
if ("/A", "Alaki.Dolaki", ".txt") != parts:
    print(f"[!] Path Parsing Error! - '{path}'")

path = "/Alaki.Dolaki.txt"
parts = get_path_parts(path=path)
if ("/", "Alaki.Dolaki", ".txt") != parts:
    print(f"[!] Path Parsing Error! - '{path}'")
