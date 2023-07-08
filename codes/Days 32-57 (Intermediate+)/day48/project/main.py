from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 
driver.get("https://orteil.dashnet.org/experiments/cookie/")

driver.maximize_window()


timer = time.time() + 3
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

        timer = timer + 3

        upd_items = [driver.find_element(By.ID, i) for i in ids]

        #take prices
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
        actual_price = driver.find_element(By.ID, "money").text
        try:
            actual_price = int(actual_price.replace(",", ""))
        except:
            actual_price = int(actual_price)
        count = []
        for i in actual_prices:
            if i<=actual_price:
                count.append(i)
        

        #up the most expensive upgrade
        try:
            most_expensive = max(count)
            index = actual_prices.index(most_expensive)
            up_id = upd_items[index]
            up_id.click()
        except ValueError:
            pass