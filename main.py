from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time


PATH = './chromedriver.exe'  # this is for chrome version 93  download from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the same folder as this file
# you can view chrome version in chrome://version, paste this in url bar and see the version number and downlaod corresponding version of chromedriver


options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # update this with your username


driver = webdriver.Chrome(executable_path=PATH, options=options)
driver.get('https://twitter.com/')

email = "xxxxxxxxxxxxxxxx@gmail.com"  # your email
password = "xxxxxxxxxxxx"  # your password

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'react-root')))
    time.sleep(3)
    # email_input = main.find_element_by_xpath(
    #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    # email_input.send_keys(email)
    # password_input = main.find_element_by_xpath(
    #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
    # password_input.send_keys(password)
    # password_input.submit()
    # time.sleep(3)
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'react-root')))
        time.sleep(2)
        tweet = "Hey, This is tweet by Selenium"
        tweetInputField = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweetInputField.send_keys(tweet)
        time.sleep(2)
        scheduleButton = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[5]')
        scheduleButton.click()

        time.sleep(2)
        selectHour = driver.find_element_by_xpath('//*[@id="SELECTOR_4"]')
        time.sleep(1)
        selectHour.send_keys("4")
        time.sleep(2)
        selectMonth = driver.find_element_by_xpath('//*[@id="SELECTOR_5"]')
        time.sleep(1)

        selectMonth.send_keys("59")
        time.sleep(2)
        selectAmPm = driver.find_element_by_xpath('//*[@id="SELECTOR_6"]')
        time.sleep(1)
        selectMonth.send_keys("AM")
        time.sleep(2)
        scheduleSubmit = driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/div')
        time.sleep(1)
        scheduleSubmit.click()
        time.sleep(2)
        tweetButton = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]')
        tweetButton.click()
    except:
        print("Error while tweeting")
except:
    print("Error while logging in")
