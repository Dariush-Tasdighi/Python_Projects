"""Simple Encryption (Encoding)"""

import os

os.system(command="cls")


def main():
    """Main Function."""

    plain_text = input("What is your text: ")

    plain_text_bytes = plain_text.encode()
    # plain_text_bytes = plain_text.encode(encoding="utf-8")

    plain_text_hex = bytes.hex(plain_text_bytes)
    print("Encoded Text: ", plain_text_hex)


if __name__ == "__main__":
    main()
