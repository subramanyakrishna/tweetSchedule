from sys import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

import os
import time

# install all required packages
# pip install selenium
# pip install webdriver_manager

PATH = './chromedriver.exe'  # this is for chrome version 93  download from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the same folder as this file
# you can view chrome version in chrome://version, paste this in url bar and see the version number and downlaod corresponding version of chromedriver
CHROME_PATH = "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
EMAIL_INPUT_XPATH = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
PSWD_INPUT_XPATH = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
TWEET_INPUT_FIELD = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div'
SCHEDULE_BUTTON = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[5]'
SELECT_HOUR = '//*[@id="SELECTOR_4"]'
SELECT_MINUTE = '//*[@id="SELECTOR_5"]'
SELECT_AM_PM = '//*[@id="SELECTOR_6"]'
SCHEDULE_SUBMIT = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/div'
TWEET_BUTTON = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]'

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + os.path.expanduser('~') + CHROME_PATH)
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(), options=options)
driver.get('https://twitter.com/login')

# update this with your username and password
email = "xxxxxxxxxxxxxxxx@gmail.com"  # your email
password = "xxxxxxxxxxxx"  # your password


def w(t):
    time.sleep(t)


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


# wait for login page or direct tweet page to arrive
main = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'react-root')))
w(3)
if(check_exists_by_xpath(EMAIL_INPUT_XPATH)):
    email_input = driver.find_element_by_xpath(EMAIL_INPUT_XPATH)
    email_input.send_keys(email)
    password_input = driver.find_element_by_xpath(PSWD_INPUT_XPATH)
    password_input.send_keys(password)
    password_input.submit()
    # wait for the login to complete
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'react-root')))
    w(2)

tweet = "Hey, This is tweet by Selenium"
tweetInputField = driver.find_element_by_xpath(TWEET_INPUT_FIELD)
tweetInputField.send_keys(tweet)
w(2)
scheduleButton = driver.find_element_by_xpath(SCHEDULE_BUTTON)
scheduleButton.click()

w(2)
selectHour = driver.find_element_by_xpath(SELECT_HOUR)
w(1)
selectHour.send_keys("4")
w(2)
selectMinite = driver.find_element_by_xpath(SELECT_MINUTE)
w(1)

selectMinite.send_keys("59")
w(2)
selectAmPm = driver.find_element_by_xpath(SELECT_AM_PM)
w(1)
selectAmPm.send_keys("AM")
w(2)
scheduleSubmit = driver.find_element_by_xpath(SCHEDULE_SUBMIT)
w(1)
scheduleSubmit.click()
w(2)
tweetButton = driver.find_element_by_xpath(
)
tweetButton.click()
