import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager





def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.facebook.com/?_rdc=1&_rdr")

    driver.find_element(By.NAME, "email").send_keys("hihdpuiyftujfgw;ukfp")
    driver.find_element(By.NAME, "pass").send_keys("*******")

    driver.find_element(By.NAME, "login").click()
    time.sleep(20)


if __name__ == '__main__':
    main()