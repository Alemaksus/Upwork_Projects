from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import vk_password

# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")


driver = webdriver.Chrome(
    executable_path="C:\\Coding\\Data Science\\Data Extraction\\Upwork_Projects\\Upwork_Projects\\Selenium\\chromedriver\\chromedriver.exe",
    options=options
)

# r"C:\Coding\Data Science\Data Extraction\Upwork_Projects\Upwork_Projects\Selenium\chromedriver\chromedriver.exe"

try:
    driver.get("https://vk.com")
    time.sleep(5)

    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys("79623618753")
    time.sleep(5)

    password_input = driver.find_element_by_id("index_pass")
    password_input.clear()
    password_input.send_keys("vk_password")
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)

    # login_button = driver.find_element_by_id("index_login_button").click()
    time.sleep(10)

    news_link = driver.find_element_by_id("l_nwsf").click()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()