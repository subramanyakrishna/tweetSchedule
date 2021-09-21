from sys import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import os
import time as t
import random
tweets = pd.read_excel('tweet.xlsx')
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
SELECT_MONTH = '//*[@id="SELECTOR_1"]'
SELECT_DAY = '//*[@id="SELECTOR_2"]'
SELECT_YEAR = '//*[@id="SELECTOR_3"]'
SELECT_HOUR = '//*[@id="SELECTOR_4"]'
SELECT_HOUR1 = '//*[@id="SELECTOR_10"]'
SELECT_HOUR2 = '//*[@id="SELECTOR_16"]'
SELECT_HOUR3 = '//*[@id="SELECTOR_22"]'
SELECT_MINUTE = '//*[@id="SELECTOR_5"]'
SELECT_MINUTE1 = '//*[@id="SELECTOR_11"]'
SELECT_MINUTE2 = '//*[@id="SELECTOR_17"]'
SELECT_MINUTE3 = '//*[@id="SELECTOR_23"]'

SELECT_AM_PM = '//*[@id="SELECTOR_6"]'
SELECT_AM_PM1 = '//*[@id="SELECTOR_12"]'
SELECT_AM_PM2 = '//*[@id="SELECTOR_18"]'
SELECT_AM_PM3 = '//*[@id="SELECTOR_24"]'

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


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def schedule(selectorIdStart, dateArr, timeArr):
    j = 2
    print(dateArr)
    print(timeArr)
    select = driver.find_element_by_xpath(
        '//*[@id="SELECTOR_{}"]'.format(selectorIdStart))
    t.sleep(2)
    select = Select(select)
    select.select_by_index(dateArr[1])
    print(dateArr[1])
    selectorIdStart += 1
    select = driver.find_element_by_xpath(
        '//*[@id="SELECTOR_{}"]'.format(selectorIdStart))
    t.sleep(2)
    select.send_keys(dateArr[0])
    print(dateArr[0])
    selectorIdStart += 2
    j = 0
    for i in range(selectorIdStart, selectorIdStart+3):
        select = driver.find_element_by_xpath(
            '//*[@id="SELECTOR_{}"]'.format(i))
        print(i)
        driver.implicitly_wait(2)
        t.sleep(2)
        select.send_keys(timeArr[j])
        print(timeArr[j])
        j += 1


# wait for login page or direct tweet page to arrive
main = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'react-root')))
driver.implicitly_wait(3)

if(check_exists_by_xpath(EMAIL_INPUT_XPATH)):
    email_input = driver.find_element_by_xpath(EMAIL_INPUT_XPATH)
    email_input.send_keys(email)
    password_input = driver.find_element_by_xpath(PSWD_INPUT_XPATH)
    password_input.send_keys(password)
    password_input.submit()
    # wait for the login to complete
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'react-root')))
    driver.implicitly_wait(3)

idStart = 1
for key, row in tweets.iterrows():
    time = row["time"]
    date = row["date"]

    dateArr = []
    timeArr = []
    if type(date) == pd._libs.tslib.Timestamp:
        day = "% s" % date.day
        month = "% s" % date.month
        year = "% s" % date.year
    else:
        [day, month, year] = date.split("-")

    [hour, min, ampm] = time.split(":")
    hour = hour.lstrip("0")
    min = min.lstrip("0")
    day = day.lstrip("0")
    month = month.lstrip("0")
    year = year.lstrip("0")

    dateArr = [day, month, year]
    timeArr = [hour, min, ampm]

    tweetInputField = driver.find_element_by_xpath(TWEET_INPUT_FIELD)
    tweetInputField.send_keys(row["tweet"])
    driver.implicitly_wait(3)
    t.sleep(5)
    scheduleButton = driver.find_element_by_xpath(SCHEDULE_BUTTON)
    scheduleButton.click()

    driver.implicitly_wait(3)
    schedule(idStart, dateArr, timeArr)
    idStart += 6
    scheduleSubmit = driver.find_element_by_xpath(SCHEDULE_SUBMIT)
    driver.implicitly_wait(3)
    scheduleSubmit.click()
    driver.implicitly_wait(3)
    tweetButton = driver.find_element_by_xpath(TWEET_BUTTON)
    tweetButton.click()
