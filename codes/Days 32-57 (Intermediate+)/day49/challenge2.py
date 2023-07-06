from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 
driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.maximize_window()
articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(articles.text)


articles.click()

searchbar = driver.find_element(By.NAME, "search")
searchbar.send_keys("TEST")
searchbar.send_keys(Keys.ENTER)



time.sleep(10)
driver.quit()