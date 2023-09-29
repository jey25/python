
from bs4 import BeautifulSoup
import requests

response = requests.get("")

soup = BeautifulSoup(response.text, "html.parser")
tags = soup.find_all(name="a", class_="storylink")

texts = []
links = []

for tag in tags:
    text = tag.get_text()
    texts.append(text)
    link = tag.get("href")
    links.append(link)


upvote = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="socre")]

largest_number = max(upvote)
largest_index = upvote.index(largest_number)

print(texts[largest_index])
print(links[largest_index])