from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Sheet():
    def __init__(self):
        service = Service("C:\Developer\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfwtLtH3jaKs2bwTmvvNbfYwTGbZPXwq4BJzTGC2ApClbxh4g/viewform?usp=sf_link")
        self.count = 1
        time.sleep(2)

    def send(self, ans):
        resp = self.driver.find_element(By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{self.count}]/div/div/div[2]/div/div[1]/div/div[1]/input')
        resp.send_keys(ans)
        if self.count == 3:
            self.count = 0
        self.count+=1
        time.sleep(1)

    def confirm(self):
        confirm = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        confirm.click()
        time.sleep(1)