from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

f_name.send_keys("Davi")
l_name.send_keys("Nasiasene")
email.send_keys("davi.nasiamorim366@gmail.com")

button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()

time.sleep(5)
driver.quit()