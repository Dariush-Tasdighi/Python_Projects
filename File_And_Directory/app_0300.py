"""Application 300"""

import os

os.system(command="cls")


def get_path_parts(path: str):
    """Get Path Parts Function."""

    if path is None:
        return None

    path = path.strip()

    if path == "":
        return None

    location, tail = os.path.split(p=path)
    # (location, tail) = os.path.split(p=path)

    items = os.path.splitext(p=tail)

    file_name = items[0]
    file_extension = items[1]

    parts = (location, file_name, file_extension)

    return parts


def test_of_get_path_parts():
    """Test of Get Path Parts Function."""

    path = None
    parts = get_path_parts(path=path)
    if parts is not None:
        print(f"[!] Path Parsing Error! - '{path}'")

    path = ""
    parts = get_path_parts(path=path)
    if parts is not None:
        print(f"[!] Path Parsing Error! - '{path}'")

    path = "     "
    parts = get_path_parts(path=path)
    if parts is not None:
        print(f"[!] Path Parsing Error! - '{path}'")

    path = "Alaki"
    parts = get_path_parts(path=path)
    if parts != ("", "Alaki", ""):
        print(f"[!] Path Parsing Error! - '{path}'")

    path = "Alaki.txt"
    parts = get_path_parts(path=path)
    if parts != ("", "Alaki", ".txt"):
        print(f"[!] Path Parsing Error! - '{path}'")

    path = "Alaki.Dolaki.txt"
    parts = get_path_parts(path=path)
    if parts != ("", "Alaki.Dolaki", ".txt"):
        print(f"[!] Path Parsing Error! - '{path}'")

    path = "     Alaki.Dolaki.txt     "
    parts = get_path_parts(path=path)
    if parts != ("", "Alaki.Dolaki", ".txt"):
        print(f"[!] Path Parsing Error! - '{path}'")

    # In Windows

    path = "C:\\A\\"
    parts = get_path_parts(path=path)
    if parts != ("C:\\A", "", ""):
        print(f"[!] Path Parsing Error! - '{path}'")

    path = "C:\\A\\Alaki.Dolaki.txt"
    parts = get_path_parts(path=path)
    if parts != ("C:\\A", "Alaki.Dolaki", ".txt"):
        print(f"[!] Path Parsing Error! - '{path}'")

    # In Linux / Mac

    path = "/A/"
    parts = get_path_parts(path=path)
    if parts != ("/A", "", ""):
        print(f"[!] Path Parsing Error! - '{path}'")

    path = "/A/Alaki.Dolaki.txt"
    parts = get_path_parts(path=path)
    if parts != ("/A", "Alaki.Dolaki", ".txt"):
        print(f"[!] Path Parsing Error! - '{path}'")

    path = "/Alaki.Dolaki.txt"
    parts = get_path_parts(path=path)
    if parts != ("/", "Alaki.Dolaki", ".txt"):
        print(f"[!] Path Parsing Error! - '{path}'")


# test_of_get_path_parts()


def main():
    """Main Function."""
    test_of_get_path_parts()


if __name__ == "main":
    main()
