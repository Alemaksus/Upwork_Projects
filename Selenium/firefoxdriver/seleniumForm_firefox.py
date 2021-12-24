from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import instagram_password

# options
options = webdriver.FirefoxOptions()

options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

driver = webdriver.Firefox(
    executable_path="C:\\Coding\\Data Science\\Data Extraction\\Upwork_Projects\\Upwork_Projects\Selenium\\firefoxdriver\\geckodriver.exe",
    options=options
)

try:
    driver.get("https://instagram.com")
    time.sleep(5)

    username_input = driver.find_element_by_name("username")
    username_input.clear()
    username_input.send_keys("python2days")
    time.sleep(5)

    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys("instagram_password")
    time.sleep(5)

    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()