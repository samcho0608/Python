# Requirement
# 1. 네이버에서 오늘 서울의 날씨정보를 가져온다
# 2. 헤드라인 뉴스 3건을 가져온다
# 3. IT 뉴스 3건을 가져온다
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화지문을 가져온다

# OUPUT EXAMPLE
# [오늘의 날씨]
# 흐림, 어제보다 00*C 높아요
# 현재 00*C (최저 00*C / 최고 00*C)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 ...
# 초미세먼지 ...

# [헤드라인 뉴스]
# 1. ...
#  (링크 : ...)
# ...

# [IT 뉴스]
# 1. ...
#  (링크 : ...)
# ...

# [오늘의 영어 회화]
# (영어 지문)
# ...

# (한글 지문)
# ...

import requests, re
from bs4 import BeautifulSoup

def scrape_weather():
    # 네이버 날씨
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # WEATHER REPORT
    print("[오늘의 날씨]") # [오늘의 날씨]

    # main weather report
    main = soup.find("div", attrs = {"class":"info_data"})
    comparison = main.find("p", attrs = {"class": "cast_txt"}).get_text()
    curr_temp = main.find("span", attrs = {"class" : "todaytemp"}).get_text()
    min_temp = main.find("span", attrs = {"class" : "min"}).span.get_text()
    max_temp = main.find("span", attrs = {"class" : "max"}).span.get_text()

    print(comparison) # 흐림, 어제보다 00*C 높아요
    print(f"현재 {curr_temp}℃ (최저 {min_temp}℃ / 최고 {max_temp}℃)") # 현재 00*C (최저 00*C / 최고 00*C)

    # Precipitation info
    morning_precipitation = soup.find("span", attrs = {"class" : "point_time morning"}).get_text().strip()
    afternoon_precipitation = soup.find("span", attrs = {"class" : "point_time afternoon"}).get_text().strip()

    print(f"오전 {morning_precipitation} / 오후 {afternoon_precipitation}", end="\n\n") # 오전 강수확률 00% / 오후 강수확률 00%

    # find dust info
    dust_table = soup.find("dl", attrs = {"class":"indicator"})
    dust_type = dust_table.find_all("dt")[:2]
    dust_info = dust_table.find_all("dd")[:2]

    # 미세먼지 ...
    # 초미세먼지 ...
    for i in range(2):
        print(dust_type[i].get_text().strip(), dust_info[i].get_text().strip())

def scrape_headline():
    # 헤드라인 뉴스
    url = "https://news.naver.com/"
    headers = {"User-Agent" :"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # HEADLINE NEWS
    print("[헤드라인 뉴스]")

    headlines = soup.find_all("div", attrs = {"class": "hdline_article_tit"})[:3]
    for i, headline in enumerate(headlines):
        link = headline.a["href"]
        print(f"{i+1}.",headline.get_text().strip())
        print(f"\t(링크 : {link})")
    print()

def scrape_IT():
    # IT 뉴스
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    headers = {"User-Agent" :"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    print("[IT 뉴스]")
    headlines = soup.find("ul", attrs = {"class" : "type06_headline"}).find_all("dt", attrs = {"class":False})[:3]

    for i, headline in enumerate(headlines):
        link = headline.a["href"]
        print(f"{i+1}.", headline.get_text().strip())
        print(f"\t(링크 : {link})")
    print()

def scrape_hackers():
    # 해커스 영어
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english#;"
    headers = {"User-Agent" :"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    print("[오늘의 영어 회화]")
    conversation_box = soup.find("div", attrs={"class" : "conv_main contentsPageWrap"})
    conversations = conversation_box.find_all("div", attrs={"class":"conv_in"})[:2]
    conversations.reverse()
    languages = ["(영어 지문)", "(한글 지문)"]

    for i, convo in enumerate(conversations):
        print(languages[i])
        for line in convo.div.find_all("div"):
            print(line.get_text().strip())
        print()

if __name__ == "__main__":
    scrape_weather()
    scrape_headline()
    scrape_IT()
    scrape_hackers()