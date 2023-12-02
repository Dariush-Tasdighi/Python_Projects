"""Dir"""

import os
import argparse

os.system(command="cls")

# Instantiate an argument parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument(
    "path",
    help="The path to the corresponding directory",
)

# Add an argument
parser.add_argument(
    "-e",
    "--echo",
    help="Display the file content",
    action="store_true",
)

# Add an argument
parser.add_argument(
    "-r",
    "--recursive",
    help="Get all files, even in sub directories",
    action="store_true",
)

# Retrieve arguments
args = parser.parse_args()

path = args.path
print("Path:", path)

echo = args.echo
print("Echo:", echo)

recursive = args.recursive
print("Recursive:", recursive)

# Validate positional arguments
if not os.path.exists(path=path):
    print("[!] Invalid path!")
    quit()

# Validate positional arguments
if not os.path.isdir(s=path):
    print("[!] path must not be a file!")
    quit()

print("Welcome")
# ********************
