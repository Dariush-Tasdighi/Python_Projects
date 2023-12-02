""" Learn 2 """

# ********************
# Test:
# python .\app_02.py
#
# - Output:
#     usage: app_02.py [-h] [-s] path
#     app.py: error: the following arguments are required: path
# ********************
# Test:
# python .\app_02.py -h
# python .\app_02.py --help
# ********************
# Test:
# python .\app_02.py Alaki
# ********************
# Test:
# python .\app_02.py Temp
# ********************
# Test:
# python .\app_02.py Temp -s
# python .\app_02.py Temp --summery
# ********************
# import os, argparse

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
    "-s",
    "--summery",
    help="Get the file summery",
    action="store_true",
)

# Retrieve arguments
args = parser.parse_args()

path = args.path
print("Path:", path)

summery = args.summery
print("Summery:", summery)

# Validate positional arguments
if not os.path.exists(path=path):
    print("[!] Invalid path!")
    quit()

print("Welcome")
# ********************
