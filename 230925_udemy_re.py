
from bs4 import BeautifulSoup
import requests

response = requests.get("")

soup = BeautifulSoup(response.text, "html.parser")

