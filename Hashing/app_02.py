"""Learning Hash (File)"""

import os
import hashlib

os.system(command="cls")


def get_md5(file: str):
    """Get MD5 Hash of File"""

    if not os.path.exists(path=file):
        return None

    if not os.path.isfile(path=file):
        return None

    md5 = hashlib.md5()
    with open(file=file, mode="rb") as file_stream:
        chunk = file_stream.read(4096)
        while len(chunk) > 0:
            md5.update(chunk)
            chunk = file_stream.read(4096)

    result = md5.hexdigest()

    return result


def main():
    """Main Function."""

    file = input("Input your file: ")

    md_hashed_password = get_md5(file=file)
    if md_hashed_password is None:
        print(f"[!] File '{file}' does not exist!")
    else:
        print(md_hashed_password, len(md_hashed_password))


if __name__ == "__main__":
    main()
