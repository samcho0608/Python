import requests, re
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=thdvk+gpffl&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

table = soup.find("div", attrs={"id":"estateCollTabContents"}).find("table", attrs = {"class":"tbl"})
headers = table.find_all("th")
rows = table.find("tbody").find_all("tr")

for i, row in enumerate(rows):
    print("=" * 10 + f"매물 {i+1}" + "=" * 10)
    for header in headers:
        print(f"{header.get_text().strip()} :", row.find("td", attrs = {"class": header["class"]}).get_text().strip())
