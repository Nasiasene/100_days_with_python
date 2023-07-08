from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
 
service = Service("C:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 
driver.get("https://www.python.org/")

driver.maximize_window()

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")
event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")


count = 0
dict = {}
while count < len(event_name):
    dict[f"{count}"] = {
        "time": dates[count].text,
        "name": event_name[count].text
    }
    count+=1

print(dict)