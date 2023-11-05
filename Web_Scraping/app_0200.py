"""Learn 200"""

import os
import requests

os.system(command="cls")

# Seconds
TIME_OUT = 5

url = input("Enter URL: ")

response = requests.get(url=url, timeout=TIME_OUT)

if response.status_code == 200:
    for key, value in response.headers.items():
        print(f"{key}: {value}")
