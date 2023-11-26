"""Application 400"""

import os

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


def main():
    """Main Function."""

    path = input("Path: ")

    file_items = get_files(path=path)

    for file_item in file_items:
        print(f"File Path: {file_item}")

        with open(file=file_item, mode="rt", encoding="utf-8") as file:
            file_content = file.read()
            print(file_content)
            print("*" * 10)


if __name__ == "__main__":
    main()
