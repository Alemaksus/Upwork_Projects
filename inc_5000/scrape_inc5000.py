"""
scraping the Inc.5000 list at https://www.inc.com/inc5000/2021
"""

import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import json


def get_data(url):

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/96.0.4664.45 Safari/537.36 "
    }
    # req = requests.get(url, headers=headers)
    # # print(req.text)
    #
    # with open("projects.html", "w") as file:
    #     file.write(req.text)

    with open("projects.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")


get_data("https://www.inc.com/inc5000/2021")

