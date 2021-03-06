import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def get_data(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru - RU, ru, q = 0.8, en - US; q = 0.5, en, q = 0.3",
        "Cache-Control": "max - age = 0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
    }

    r = requests.get(url=url, headers=headers)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(r.text)

    # get hotels urls
    # print(r.text)
    soup = BeautifulSoup(r.text, "lxml")

    hotels_cards = soup.find_all("div", class_="hotels_card_dv")

    for hotel_url in hotels_cards:
        hotel_url = hotel_url.find("a").get("href")
        # print(hotel_url)


def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0")

    try:
        driver = webdriver.Firefox(
            executable_path="C:\\Coding\\Data Science\\Data Extraction\\Upwork_Projects\\Upwork_Projects\\Tury\\geckodriver",
            options=options
        )
        driver.get(url=url)
        time.sleep(5)

        with open("index_selenium.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    with open("index_selenium.html") as file:
        src = file.read()

    # get hotels urls
    soup = BeautifulSoup(src, "lxml")

    hotels_cards = soup.find_all("div", class_="hotel_card_dv")

    for hotel_url in hotels_cards:
        hotel_url = "https://www.tury.ru" + hotel_url.find("a").get("href")
        print(hotel_url)


def main():
    # get_data("https://www.tury.ru/hotel/most_luxe.php")
    get_data_with_selenium("https://www.tury.ru/hotel/most_luxe.php")


if __name__ == "__main__":
    main()
