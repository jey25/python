
# from bs4 import BeautifulSoup
# import requests

# response = requests.get("")

# soup = BeautifulSoup(response.text, "html.parser")
# tags = soup.find_all(name="a", class_="storylink")

# texts = []
# links = []

# for tag in tags:
#     text = tag.get_text()
#     texts.append(text)
#     link = tag.get("href")
#     links.append(link)


# upvote = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="socre")]

# largest_number = max(upvote)
# largest_index = upvote.index(largest_number)

# print(texts[largest_index])
# print(links[largest_index])



# 꼭 봐야 할 영화 100선 프로젝트
# https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/

# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

# soup = BeautifulSoup(response.text, "html.parser")
# titles = soup.find_all(name="h3", class_="title")

# texts = []

# for title in titles:
#     text = title.get_text()
#     texts.append(text)

# texts.reverse()
# results = '\n'.join(texts)

# print(results)

# with open("result.txt", mode="w") as file:
#     for result in results:
#         file.write(f"{result}")



# Billnoard hot 100 스크래핑

# from bs4 import BeautifulSoup
# import requests

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD : ")
# url = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
# soup = BeautifulSoup(url.text, "html.parser")

# titles = []

# lists = soup.select("li ul li h3")

# for list in lists:
#     title = list.get_text().strip()
#     titles.append(title)

# print(titles)









