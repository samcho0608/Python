import requests
url = "http://nadocoding.tistory.com"
# web sites have headers where they get the user info aka user-agent to determine what they will show
# e.g. the type of device/browser, whether its web scraping/crawling or not etc.
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)