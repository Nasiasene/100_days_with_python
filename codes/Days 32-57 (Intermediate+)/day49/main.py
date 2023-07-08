from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

#EMAIL=os.environ["EMAIL"]
#PASSWORD=os.environ["PASSWORD"]

service = Service("C:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

driver.maximize_window()

time.sleep(5)

button = driver.find_element(By.XPATH, "/html/body/div[3]/a[1]")
print(button.text)
driver.quit()