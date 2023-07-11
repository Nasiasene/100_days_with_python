from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


EMAIL=os.environ["EMAIL"]
PASSWORD=os.environ["PASSWORD"]

service = Service("C:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

driver.maximize_window()

#Openning linkedin and sign up
time.sleep(1)
button = driver.find_element(By.XPATH, "/html/body/div[3]/a[1]")
button.click()

email_answer = driver.find_element(By.ID, 'username')
email_answer.send_keys(EMAIL)
password_answer =driver.find_element(By.ID, 'password')
password_answer.send_keys(PASSWORD)
check_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
check_button.click()
time.sleep(3)

#Saving
page = driver.find_elements(By.CSS_SELECTOR, "ul.scaffold-layout__list-container li")
for i in page:
    i.click()
    time.sleep(0.5)
    save_button = driver.find_element(By.CSS_SELECTOR, '.display-flex .jobs-save-button')
    save_button.click()

time.sleep(10)
driver.quit()