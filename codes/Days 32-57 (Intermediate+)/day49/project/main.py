from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 
driver.get("https://orteil.dashnet.org/experiments/cookie/")

driver.maximize_window()


timer = time.time() + 5
final_time = time.time() + 5*60


cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
ids = []
for i in items:
    ids.append(i.get_attribute("id"))


while True:
    cookie.click()

    if time.time() > final_time:
        cookie_s = driver.find_element(By.ID, "cps").text
        print(cookie_s.split(": ")[1])
        break

    if time.time() > timer:

        timer = timer + 5

        upd_items = [driver.find_element(By.ID, i) for i in ids]

        #colet prices
        actual_prices = []
        for i in upd_items:
            text = i.text
            text = text.split('\n')[0] #for i in actual_prices if len(i.split("\n")) != 1]
            try:
                text = text.split(" - ")[1]
                try:
                    text = text.replace(",", "")
                    actual_prices.append(int(text))
                except:
                    actual_prices.append(int(text))
            except IndexError:
                pass
 

        #checking prices
        actual_price = driver.find_element(By.ID, "money")

