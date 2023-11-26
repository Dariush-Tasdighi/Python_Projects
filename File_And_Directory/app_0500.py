"""Application 500"""

import os

os.system(command="cls")


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

    # for path, folders, files in os.walk(top=path):
    #     path_items = [os.path.join(path, file) for file in files]
    #     file_items.extend(path_items)

    return file_items


def main():
    """Main Function."""

    path = input("Path: ")

    file_items = get_all_files(path=path)

    for file_item in file_items:
        print(f"File Path: {file_item}")


if __name__ == "__main__":
    main()
