import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# find a list of all webtoons currently being published on the comic.naver.com
cartoons = soup.find_all("a", attrs={"class":"title"}) # find all a tags whose class is title
print([cartoon.get_text() for cartoon in cartoons])