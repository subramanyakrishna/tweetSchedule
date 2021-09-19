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


class Driver:
    def __init__(self, email, password):
        driver.get('https://twitter.com/login')
        self.email = email  # your email
        self.password = password  # your password
        try:
            main = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'react-root')))
            email_input = main.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            email_input.send_keys(email)
            self.w(1)
            password_input = main.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            password_input.send_keys(password)
            password_input.submit()
            w(3)
        except:
            print('')

    def w(t):
        w(t)

    def tweetSchedule():
