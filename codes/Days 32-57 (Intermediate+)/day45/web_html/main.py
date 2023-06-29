from bs4 import BeautifulSoup
import requests as r

response = r.get("https://news.ycombinator.com/news") #to get data
html = response.text #transform to html

soup = BeautifulSoup(html, "html.parser")

texts = soup.find_all(name="span", class_="titleline")
titles = []
link = []
for t in texts:
    titles.append(t.a.getText())
    link.append(t.a.get('href'))

score = soup.find_all(name="span", class_="score")
scores = []
for p in score:
    s = p.getText()
    scores.append(int(s.split(" points")[0]))


max_index = scores.index(max(scores))
print(f"{titles[max_index]}\n{link[max_index]}\n{scores[max_index]}")