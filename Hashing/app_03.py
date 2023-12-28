"""Learning Hash (File)"""

import os
import sys
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


def get_sha1(file: str):
    """Get SHA1 Hash of File"""

    if not os.path.exists(path=file):
        return None

    if not os.path.isfile(path=file):
        return None

    sha1 = hashlib.sha1()
    with open(file=file, mode="rb") as file_stream:
        chunk = file_stream.read(4096)
        while len(chunk) > 0:
            sha1.update(chunk)
            chunk = file_stream.read(4096)

    result = sha1.hexdigest()

    return result


def get_sha256(file: str):
    """Get SHA256 Hash of File"""

    if not os.path.exists(path=file):
        return None

    if not os.path.isfile(path=file):
        return None

    sha256 = hashlib.sha256()
    with open(file=file, mode="rb") as file_stream:
        chunk = file_stream.read(4096)
        while len(chunk) > 0:
            sha256.update(chunk)
            chunk = file_stream.read(4096)

    result = sha256.hexdigest()

    return result


def main():
    """Main Function."""

    file = input("Input your file: ")

    if not os.path.exists(path=file):
        print(f"[!] File '{file}' does not exist!")
        sys.exit()

    if not os.path.isfile(path=file):
        print(f"[!] File '{file}' does not exist!")
        sys.exit()

    md_hashed_password = get_md5(file=file)
    sha1_hashed_password = get_sha1(file=file)
    sha256_hashed_password = get_sha256(file=file)

    print("MD5   : ", md_hashed_password, "Length: ", len(md_hashed_password))
    print("SHA1  : ", sha1_hashed_password, "Length: ", len(sha1_hashed_password))
    print("SHA256: ", sha256_hashed_password, "Length: ", len(sha256_hashed_password))


if __name__ == "__main__":
    main()
