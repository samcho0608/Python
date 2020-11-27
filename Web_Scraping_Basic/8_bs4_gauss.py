import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# print(cartoons[0].a.get_text())

# link = cartoons[0].a["href"]
# print("https://comic.naver.com" + link)

# Scraping title and the links of each vol.
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# Scraping the reviews

total_review = 0
reviews = soup.find_all("div", attrs={"class":"rating_type"})
for review in reviews:
    rate = review.find("strong").get_text()
    print(rate)
    total_review += float(rate)

print("%.2f" % (total_review))
print("%.2f" % (total_review/len(reviews)))