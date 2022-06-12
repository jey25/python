from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://news.naver.com/")

bsObject = BeautifulSoup(html, "html.parser")

#뉴스 링크 가져오기
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))

#뉴스 이미지 가져오기
for link in bsObject.find_all('img'):
    print(link.text.strip(), link.get('src'))

# github test