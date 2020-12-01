# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/top"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
#     "Accept-Language" : "ko-KR,ko"
# }

# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs = {"class" : "ImZGtf mpg5gc"})
# print(len(movies))

# for movie in movies:
#     title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
#     print(title)

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# going to the page
url = "https://play.google.com/store/movies/top"
browser.get(url)

# scroll down
# scroll down to the bottom
# scroll down by the height of the resolution(in my case 1080)
browser.execute_script("window.scrollTo(0, 1080)") # the second argument is the display resolution
                                                   # in my case, it was 1920 x 1080
