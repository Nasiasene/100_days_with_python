import requests as r
from bs4 import BeautifulSoup
import re

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
params = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
        }


response = r.get(URL, headers=params)
html = response.text

soup = BeautifulSoup(html, "html.parser")

def get_lists():
    old_prices = soup.select("span.PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")
    old_prices = [i.text for i in old_prices]
    prices = []
    for i in old_prices:
        number = re.findall(r'\d+', i) #Searching numerics in the str
        numbers = [n for n in number]
        n = int(numbers[0] + numbers[1])
        prices.append(n)

    propetrty_card = soup.find_all(name="a", class_='property-card-link')
    adress = [i.text for i in propetrty_card if i.text!='']

    old_links = [i.get('href') for i in propetrty_card if i.get('href')!=None ]
    old_links= list(dict.fromkeys(old_links)) #Removing duplicate items
    links = []
    for i in old_links:
        if "https:" not in i:
            i = "https://www.zillow.com" + i
        links.append(i)

    return [adress, prices, links]