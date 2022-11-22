# Challenge 2

# Using the firefox  browser    navigate  to https://www.google.com/
# enter  the text  Python in the search  box, then  send  the  Enter  key.
# Get  the text  from  the Wikipedia brief on the  right side and  print the  value in the console.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.find_element(By.NAME, "q").send_keys("python")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    wikipedia = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/span[1]')
    print(wikipedia.text)
    time.sleep(3)



if __name__ == '__main__':
    main()
