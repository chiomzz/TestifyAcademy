# Challenge 4

# Navigate to https://www.bbc.com/ and print out the top 10 latest news from the home page.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    driver.maximize_window()
    new1 = driver.find_element(By.CLASS_NAME, "media__link")
    print(new1.text)

    new2 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[3]/div[1]/ul[1]/li[2]/div[1]/div[2]/h3[1]/a[1]")
    print(new2.text)

    new3 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[3]/div[1]/ul[1]/li[3]/div[1]/div[2]/h3[1]/a[1]")
    print(new3.text)

    number4 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[3]/div[1]/ul[1]/li[4]/div[1]/div[2]/h3[1]/a[1]")
    print(number4.text)

    number5 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[3]/div[1]/ul[1]/li[5]/div[1]/div[2]/h3[1]/a[1]")
    print(number5.text)

    number5 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[4]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/ul[1]/li[2]/div[1]/a[1]")
    print(number5.text)

    number6 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[4]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/ul[1]/li[3]/div[1]/a[1]")
    print(number6.text)

    number7 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[4]/div[1]/div[1]/div[2]/div[1]/section[2]/div[1]/ul[1]/li[1]/div[1]/a[1]")
    print(number7.text)

    number8 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[4]/div[1]/div[1]/div[2]/div[1]/section[2]/div[1]/ul[1]/li[3]/div[1]/a[1]")
    print(number8.text)
    #
    number9 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[4]/div[1]/div[1]/div[2]/div[1]/section[3]/div[1]/ul[1]/li[1]/div[1]/a[1]")
    print(number9.text)

    number10 = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[@id='page']/section[4]/div[1]/div[1]/div[2]/div[1]/section[3]/div[1]/ul[1]/li[2]/div[1]/a[1]")
    print(number10.text)
    time.sleep(3)



if __name__ == '__main__':
    main()