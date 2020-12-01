import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "Accept-Language" : "ko-KR,ko"
}

# the Accept Language header means if there is a version of the website in preferred language, show that version
# otherwise, show the original page

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs = {"class" : "ImZGtf mpg5gc"})
print(len(movies))
# this will only print out 10 bc the website is dynamic not static

# with open("Web_Scraping_Basic/movies.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
#     # writes the html file in more readable format

for movie in movies:
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
    print(title)