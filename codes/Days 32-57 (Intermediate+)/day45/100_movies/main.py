import requests as r
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = r.get(URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")

titles = soup.find_all("h3", "title")
list = [i.getText() for i in titles]
list = list[::-1]

while True:
    resp = int(input("Do you want a random moovie(0) or do you want the entire list(1)?  "))
    if resp == 1:
        for i in list:
            print(i)
        break
    elif resp == 0:
        import random as rd
        filme = rd.choice(list)
        print(filme.split(") ")[1])
        break
    else:
        print("\nChoose a valid option.\n")