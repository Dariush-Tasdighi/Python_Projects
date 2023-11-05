"""Learn 300"""

import os
import requests

os.system(command="cls")

# Seconds
TIME_OUT = 5

url = input("Enter URL: ")

try:
    response = requests.get(url=url, timeout=TIME_OUT)

    if response.status_code == 200:
        for key, value in response.headers.items():
            print(f"{key}: {value}")
except requests.exceptions.ReadTimeout as e:
    print(f"[!] Read Timeout on {url}!")

except requests.exceptions.ConnectionError as e:
    print(f"[!] Connection Error on {url}!")
