"""Display Path / File Hash(es)"""

import os
import sys
import hashlib
import argparse

os.system(command="cls")


def get_files(path: str):
    """Get Files Function."""

    file_items = []

    if path is None:
        return file_items

    path = path.strip()

    if path == "":
        return file_items

    if not os.path.exists(path=path):
        return file_items

    if os.path.isfile(path=path):
        file_items.append(path)
        return file_items

    items = os.listdir(path=path)

    for item in items:
        path_item = os.path.join(path, item)
        if os.path.isfile(path=path_item):
            file_items.append(path_item)

    return file_items


def get_all_files(path: str):
    """Get All Files Function."""

    file_items = []

    if path is None:
        return file_items

    path = path.strip()

    if path == "":
        return file_items

    if not os.path.exists(path=path):
        return file_items

    if os.path.isfile(path=path):
        file_items.append(path)
        return file_items

    for path, _, files in os.walk(top=path):
        path_items = [os.path.join(path, file) for file in files]
        file_items.extend(path_items)

    return file_items


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


def diplay_file_name_and_hashes(file: str, md5: bool, sha1: bool, sha256: bool):
    """Display File Name and It's Hashes"""

    print("*" * 50)
    print("File:", file)

    if md5 is True:
        hash_of_md5 = get_md5(file=file)
        print("MD5:", hash_of_md5)

    if sha1 is True:
        hash_of_sha1 = get_sha1(file=file)
        print("SHA-1:", hash_of_sha1)

    if sha256 is True:
        hash_of_sha256 = get_sha256(file=file)
        print("SHA-256:", hash_of_sha256)


def main():
    """Main Function."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "path",
        help="The path to the corresponding directory",
    )

    parser.add_argument(
        "-5",
        "--md5",
        help="Display the MD5 file content",
        action="store_true",
    )

    parser.add_argument(
        "-1",
        "--sha1",
        help="Display the SHA-1 file content",
        action="store_true",
    )

    parser.add_argument(
        "-256",
        "--sha256",
        help="Display the SHA-256 file content",
        action="store_true",
    )

    parser.add_argument(
        "-r",
        "--recursive",
        help="Get all files, even in sub directories",
        action="store_true",
    )

    args = parser.parse_args()

    path = args.path
    # print("Path:", path)

    md5 = args.md5
    # print("MD5:", md5)

    sha1 = args.sha1
    # print("SHA-1:", sha1)

    sha256 = args.sha256
    # print("SHA-256:", sha256)

    recursive = args.recursive
    # print("Recursive:", recursive)

    if md5 is False and sha1 is False and sha256 is False:
        print("[!] You should select at least one of the switches (md5, sha1, sha256)!")
        sys.exit()

    if not os.path.exists(path=path):
        print(f"[!] The path '{path}' does not exist!")
        sys.exit()

    if os.path.isfile(path=path):
        diplay_file_name_and_hashes(file=path, md5=md5, sha1=sha1, sha256=sha256)
    else:
        if recursive:
            files = get_all_files(path=path)
        else:
            files = get_files(path=path)

        for file in files:
            diplay_file_name_and_hashes(file=file, md5=md5, sha1=sha1, sha256=sha256)

    print("*" * 50)


if __name__ == "__main__":
    main()
