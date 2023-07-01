from bs4 import BeautifulSoup
import requests as r

bilboard_url = "https://www.billboard.com/charts/hot-100/"

choosen_date = input("Which period do you want to see? (Type in YYYY-MM-DD): ")

bilboard_url = f"{bilboard_url}{choosen_date}"

response = r.get(bilboard_url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
title = soup.select("li ul li h3")
title_list = []
for t in title:
    title_list.append(t.getText().strip())
