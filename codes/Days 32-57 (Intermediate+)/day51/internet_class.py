from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot():
    def __init__(self):
        service = Service("C:\Developer\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(2)
        start = self.driver.find_element(By.CLASS_NAME, "start-text")
        start.click()
        while True:
            try:
                self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
                self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
                break
            except:
                pass
        

    def tweet_at_provider(self, tweet, name, password):
        self.driver.get("https://twitter.com/login")
        self.driver.maximize_window()
        time.sleep(2)
        input_name = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        input_name.send_keys(name)
        input_name.send_keys(Keys.ENTER)
        time.sleep(2)
        input_password = self.driver.find_element(By.NAME, 'password')
        input_password.send_keys(password)
        input_password.send_keys(Keys.ENTER)

        time.sleep(5)
        message = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        message.send_keys(tweet)

        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/span').click()

        time.sleep(1)
        self.driver.quit()