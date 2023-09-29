
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


upvote = [score.get_text() for score in soup.find_all(name="span", class_="socre")]
