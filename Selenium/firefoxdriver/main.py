# from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = "https://www.vk.com/"

# options
options = webdriver.FirefoxOptions()

# change useragent
useragent = UserAgent()
# options.set_preference("general.useragent.override", "Hello Friend")
options.set_preference("general.useragent.override", useragent.random)

# set proxy:
# proxy = "138.128/91.65:8000"
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities["marionette"] = True
#
# firefox_capabilities["proxy"] = {
#     "proxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
# }

proxy_options = {
    "proxy": {
        "https": f"https://{login}:{password}@138.128/91.65:8000"
    }
}

# driver = webdriver.Firefox(
#     executable_path="C:\\Coding\\Data Science\\Data Extraction\\Upwork_Projects\\Upwork_Projects\Selenium\\firefoxdriver\\geckodriver.exe",
#     options=options, proxy=proxy
# )

driver = webdriver.Firefox(
    executable_path="C:\\Coding\\Data Science\\Data Extraction\\Upwork_Projects\\Upwork_Projects\Selenium\\firefoxdriver\\geckodriver.exe",
    selenium_options=proxy_options
)

try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # driver.save_screenshot("vk.png")
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