"""Learn 100"""

# **************************************************
# pip install requests
# https://github.com/psf/requests
# https://requests.readthedocs.io/en/latest
# **************************************************
# import os, requests

import os
import requests

os.system(command="cls")

# Seconds
TIME_OUT = 5

# URL = "https://dtapp.ir"
url = input("Enter URL: ")

response = requests.get(url=url, timeout=TIME_OUT)

# print(response)
# print(response.status_code)
# print(response.headers)

for key, value in response.headers.items():
    print(f"{key}: {value}")
# **************************************************
