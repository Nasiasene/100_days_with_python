import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
 
service = Service("C:\Developer\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 
driver.get("https://www.amazon.com.br/Monitor-Gamer-AOC-FreeSync-24G2/dp/B088L2GXBZ/?_encoding=UTF8&pd_rd_w=4dO3K&content-id=amzn1.sym.b984772f-84a1-42a5-ad41-901cc4abe69d&pf_rd_p=b984772f-84a1-42a5-ad41-901cc4abe69d&pf_rd_r=C4F52AM1AK86YX2NDSRW&pd_rd_wg=O7L3f&pd_rd_r=a9128c52-ec2a-43f7-aa2f-f872d446870c&ref_=pd_gw_ci_mcx_mr_hp_atf_m")


name = driver.find_element(By.ID, "productTitle")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
link = driver.find_element(By.CSS_SELECTOR, "#centerCol a")
res = driver.find_element(By.XPATH, '//*[@id="productOverview_feature_div"]/div/table/tbody/tr[2]/td[2]/span')
print(name.text)
print(price.text)
print(link.text)
print(res.text)



time.sleep(3)
driver.quit()