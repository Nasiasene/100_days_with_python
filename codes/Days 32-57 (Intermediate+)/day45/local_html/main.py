from bs4 import BeautifulSoup

file = open(r"C:\Users\davit\Documents\100days_python.py\100_days_with_python\codes\Days 32-57 (Intermediate+)\day45\website.html", encoding="utf-8")
content = file.read()
file.close()

soup = BeautifulSoup(content, 'html.parser')
print(soup.title.string, "\n\nPARAGRAPHS:")

paragraphs = soup.find_all(name="p")
for i in paragraphs:
    print(i.getText())

print("\n\nLinks:")
ancor_tags = soup.find_all("a")
for i in ancor_tags:
    print(f"Str: {i.getText()} // Link: {i.get('href')}")

heading = soup.find(name="h1", id="name")


url = soup.select_one(selector="p a")
all_url = soup.select(selector="a")