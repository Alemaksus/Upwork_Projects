# from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = "https://www.instagram.com/"

user_agents_list = [
    "hello_world",
    "best_of_the_best",
    "python_today"
]

useragent = UserAgent()

# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld:)")
# options.add_argument("user-agent=Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
# options.add_argument(f"user-agent={useragent.opera}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy:
# options.add_argument("--proxy-server=138.128/91.65:8000")

proxy_options = {
    "proxy": {
        "https": f"https://{login}:{password}@138.128/91.65:8000"
    }
}

# driver = webdriver.Chrome(
#     executable_path="C:\\Coding\\Data Science\\Data Extraction\\Upwork_Projects\\Upwork_Projects\\Selenium\\chromedriver\\chromedriver.exe",
#     options=options
# )

driver = webdriver.Chrome(
    executable_path="C:\\Coding\\Data Science\\Data Extraction\\Upwork_Projects\\Upwork_Projects\\Selenium\\chromedriver\\chromedriver.exe",
    seleniumwire_options=proxy_options
)

# r"C:\Coding\Data Science\Data Extraction\Upwork_Projects\Upwork_Projects\Selenium\chromedriver\chromedriver.exe"

try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # time.sleep(5)
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)

    driver.get("https://2ip.ru")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()