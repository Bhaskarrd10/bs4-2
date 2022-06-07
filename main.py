from bs4 import BeautifulSoup
#import lxml

with open ("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.prettify())
#print(soup.a)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    tag.get("href")
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)