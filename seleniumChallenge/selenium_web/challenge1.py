# Challenge1
# Using the chrome browser navigate to
# https://www.facebook.com/ fill  in  the  email/phone  and
# password text box then click the Login Button.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.find_element(By.NAME, "email").send_keys("dgdcggfgfgfcytc")
    driver.find_element(By.NAME, "pass").send_keys("password")
    time.sleep(4)
    driver.find_element(By.NAME, "login").click()
    time.sleep(4)


if __name__ == '__main__':
    main()
