"""Application 500"""

import os

os.system(command="cls")


def get_all_files(path: str):
    """Get All Files Function."""

    items = []

    if path is None:
        return items

    path = path.strip()

    if path == "":
        return items

    if not os.path.exists(path=path):
        return items

    if os.path.isfile(path=path):
        items.append(path)
        return items

    # for path, folders, files in os.walk(top=path):
    #     file_paths = [os.path.join(path, file) for file in files]
    #     items.extend(file_paths)

    for path, _, files in os.walk(top=path):
        file_paths = [os.path.join(path, file) for file in files]
        items.extend(file_paths)

    return items


def main():
    """Main Function."""

    path = input("Path: ")

    file_path_items = get_all_files(path=path)

    for file_path_item in file_path_items:
        print(f"File Path: {file_path_item}")


if __name__ == "__main__":
    main()
