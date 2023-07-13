from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

class InstaFollower():
    def __init__(self):
        service = Service("C:\Developer\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def login(self, email, password):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)

        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        username_input.send_keys(email)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)        

    def find_followers(self, account):
        self.driver.get(url=f"https://www.instagram.com/{account}/")
        time.sleep(5)

        followers = self.driver.find_element(By.CSS_SELECTOR, "li.xl565be a.x1i10hfl")
        followers.click()
        time.sleep(5)

    def follow(self):
        follow_people = self.driver.find_elements(By.CSS_SELECTOR, ".x1dm5mii .x9f619 .x1n2onr6 .x78zum5 button ._aacl")
        for i in follow_people:
            time.sleep(1)
            try:
                i.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.CSS_SELECTOR, '.x1cy8zhl button._a9_1')
                cancel_button.click()