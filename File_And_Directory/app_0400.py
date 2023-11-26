"""Application 400"""

import os

os.system(command="cls")


def get_files(path: str):
    """Get Files Function."""

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

    file_items = os.listdir(path=path)

    for file_item in file_items:
        path_name = os.path.join(path, file_item)
        if os.path.isfile(path=path_name):
            items.append(path_name)

    return items


def main():
    """Main Function."""

    path = input("Path: ")

    file_path_items = get_files(path=path)

    for file_path_item in file_path_items:
        print(f"File Path: {file_path_item}")

        with open(file=file_path_item, mode="rt", encoding="utf-8") as file:
            file_content = file.read()
            print(file_content)
            print("*" * 10)


if __name__ == "__main__":
    main()
