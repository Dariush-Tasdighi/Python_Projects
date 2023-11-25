"""Learning Working with File (Note: This is docstring!)"""

import os

os.system(command="cls")

# **************************************************
# # Bad Practice
# # import os, io

# # Best Practice
# import os
# import io
# **************************************************

# **************************************************
# PATH = "temp.txt"

# # ما معمولا (صرفا) از دستور ذیل استفاده می‌کنیم
# file = open(file=PATH)

# # file = io.open(file=PATH)
# # file = os.open(path=PATH)
# # file = os.fdopen(os.open(path=PATH, flags=os.O_RDONLY))
# **************************************************

# **************************************************
# *** Solution (1) *********************************
# **************************************************
# file = open("file.txt", "wt", "utf-8")
# file = open(file="file.txt", mode="w", encoding="utf-8")
file = open(file="file.txt", mode="wt", encoding="utf-8")

file.write("Hello, World (1)!")
file.write("Hello, World (2)!")
file.write("Hello, World (3)!")

file.close()
# **************************************************

# **************************************************
# file = open(file="file.txt", mode="wt", encoding="utf-8")

# # file.write("Hello, World (1)!\n")

# file.write("Hello, World (1)!")
# file.write("\n")
# file.write("Hello, World (2)!")
# file.write("\n")
# file.write("Hello, World (3)!")

# # New Line:
# #   Windows     : \r\n
# #   MacOS, Linux: \n

# # Note: Python will convert \n to os.linesep -> Line Separator

# file.close()
# **************************************************

# **************************************************
# What is os.linesep?
# **************************************************
# print("\r\n")
# print("\r\n".encode())
# print(b"\r\n")
# **************************************************

# **************************************************
# print("Hello")
# print("\r")
# print("Hello")
# print("\n")
# print("Hello")
# print(os.linesep)
# print(os.linesep.encode())
# **************************************************

# **************************************************
# Bad Practice
# **************************************************
# file = open(file="file.txt", mode="wt", encoding="utf-8")

# file.write("Hello, World (1)!")
# file.write(os.linesep)
# file.write("Hello, World (2)!")
# file.write(os.linesep)
# file.write("Hello, World (3)!")

# file.close()
# **************************************************

# **************************************************
# file = open(file="file.txt", mode="at", encoding="utf-8")

# file.write("Hello, World (4)!")
# file.write("\n")
# file.write("Hello, World (5)!")
# file.write("\n")
# file.write("Hello, World (6)!")

# file.close()
# **************************************************

# **************************************************
# *** Solution (2) *********************************
# **************************************************
# Modern Writing!
# **************************************************
# # file = open(file="file.txt", mode="wt", encoding="utf-8")

# with open(file="file.txt", mode="wt", encoding="utf-8") as file:
#     file.write("Hello, World (1)!")
#     file.write("\n")
#     file.write("Hello, World (2)!")
#     file.write("\n")
#     file.write("Hello, World (3)!")

# # Note: در این روش، دیگر نیازی به دستور ذیل نیست
# # file.close()
# **************************************************

# **************************************************
# Modern Reading!
# **************************************************
# # file_name = input("File: ")
# # file_name = "file.txt"

# # FILE_NAME = "alaki.txt"
# # FILE_NAME = "my_folder"
# FILE_NAME = "file.txt"

# if not os.path.exists(path=FILE_NAME):
#     print(f"'{FILE_NAME}' file does not exist!")
#     quit()
#     # exit()

# if not os.path.isfile(path=FILE_NAME):
#     print(f"'{FILE_NAME}' is a folder and not a file!")
#     quit()
#     # exit()

# with open(file=FILE_NAME, mode="rt", encoding="utf-8") as file:
#     file_content = file.read()
#     print(file_content)
# **************************************************
