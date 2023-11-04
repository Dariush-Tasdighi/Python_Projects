"""Learning Working with File (Note: This is docstring!)"""
import os

os.system(command="cls")

# **************************************************
# https://docs.python.org/3/tutorial/inputoutput.html
# https://docs.python.org/3/library/functions.html#open
# https://www.programiz.com/python-programming/file-operation
# https://www.linkedin.com/pulse/python-osopen-vs-built-in-open-nelson-ateya/
# https://stackoverflow.com/questions/15039528/what-is-the-difference-between-os-open-and-os-fdopen-in-python/15039662
# **************************************************
# In Python 2, the built-in open and io.open were different
# (io.open was newer and supported more things). In Python 3,
# open and io.open are now the same thing (they got rid of
# the old built-in open), so you should always use open.
# Code that needs to be compatible with Python 2 and 3
# might have a reason to use io.open.
#
# So os.open() is the default opener for open(),
# and we also have the ability to specify a custom wrapper
# around it if file flags or mode need to be changed
#
# In short, open() creates new file objects, os.open()
# creates OS-level file descriptors, and os.fdopen()
# creates a file object out of a file descriptor.
# **************************************************

# **************************************************
# Bad Practice
# import os, io

# Best Practice
# import os
# import io

# PATH = "temp.txt"

# file = open(file=PATH)
# file = io.open(file=PATH)

# file = os.open(path=PATH)
# file = os.fdopen(os.open(path=PATH, flags=os.O_RDONLY))
# **************************************************

# **************************************************
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	open for exclusive creation, failing if the file already exists
# 'a'	open for writing, appending to the end of file if it exists
# '+'	open for updating (reading and writing)
#
# 'b'	binary mode
# 't'	text mode (default)
# **************************************************

# **************************************************
# r     rt      rb
# w     wt      wb
# a     at      ab
# **************************************************

# **************************************************
# *** Solution (1) *********************************
# **************************************************
# # file = open("file.txt", "wt", "utf-8")
# # file = open(file="file.txt", mode="w", encoding="utf-8")
# file = open(file="file.txt", mode="wt", encoding="utf-8")

# file.write("Hello, World (1)!")
# file.write("Hello, World (2)!")
# file.write("Hello, World (3)!")

# file.close()
# **************************************************

# **************************************************
# file = open(file="file.txt", mode="wt", encoding="utf-8")

# # file.write("Hello, World (1)!\n")

# file.write("Hello, World (1)!")
# file.write("\n")
# file.write("Hello, World (2)!")
# file.write("\n")
# file.write("Hello, World (3)!")

# # Windows       : \r\n
# # MacOS, Linux  : \n

# # Note: Python will convert \n to os.linesep

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
# # FILE_NAME = "MyFolder"
# FILE_NAME = "file.txt"

# if not os.path.exists(path=FILE_NAME):
#     print(f"'{FILE_NAME}' file does not exist!")
#     quit()
#     # exit()

# if not os.path.isfile(path=FILE_NAME):
#     print(f"'{FILE_NAME}' is a folder and is not a file!")
#     quit()
#     # exit()

# with open(file=FILE_NAME, mode="rt", encoding="utf-8") as file:
#     file_content = file.read()
#     print(file_content)
# **************************************************
