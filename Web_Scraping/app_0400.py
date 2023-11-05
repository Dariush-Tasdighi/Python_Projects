"""Learn 400"""
# ********************
# pip install beautifulsoup4
# https://www.crummy.com/software/BeautifulSoup/bs4
# ********************
# https://www.freeproxy.world/
# ********************
import os
import requests
from bs4 import BeautifulSoup

os.system(command="cls")

# Seconds
TIME_OUT = 5

# url = input("Enter URL: ")
URL = "https://www.laliga.com/en-GB/laliga-easports/standing"

try:
    response = requests.get(url=URL, timeout=TIME_OUT)

    if response.status_code == 200:
        # for key, value in response.headers.items():
        #     print(f"{key}: {value}")

        # print(response.text)

        soup = BeautifulSoup(response.text, "html.parser")

        # items = soup.find_all(name="p", attrs={"class": "hOVgXP"})
        # items = soup.find_all(
        #     name="p", attrs={"class": "styled__TextStyled-sc-1mby3k1-0"}
        # )
        # items = soup.find_all(
        #     name="p", attrs={"class": "styled__TextStyled-sc-1mby3k1-0 hOVgXP"}
        # )

        # for item in items:
        #     title = item.get_text()
        #     print(title)

        div_items = soup.find_all(
            name="div",
            attrs={
                "class": "styled__ShieldContainer-sc-1opls7r-0 eIaTDi shield-desktop"
            },
        )

        for div_item in div_items:
            p_items = div_item.find_all(
                name="p",
                attrs={"class": "styled__TextStyled-sc-1mby3k1-0 hOVgXP"},
            )

            for p_item in p_items:
                title = p_item.get_text()
                print(title)

except requests.exceptions.ReadTimeout as e:
    print(f"[!] Read Timeout on {URL}!")

except requests.exceptions.ConnectionError as e:
    print(f"[!] Connection Error on {URL}!")
