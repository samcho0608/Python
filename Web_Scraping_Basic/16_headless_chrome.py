from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True             # runs chrome in the background instead of opening it on GUI
options.add_argument("window-size=1920x1080")   # sets the size of the window

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# going to the page
url = "https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 2 # 2 초에 한번씩 스크롤 내림

# store the current page height in a variable
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # scroll to the bottom of the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # wait for page loading to finish
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("scroll finished")
browser.get_screenshot_as_file("Web_Scraping_Basic/google_movie.png") # takes the screenshot of the page


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs = {"class" : ["ImZGtf mpg5gc", "Vpfmgd"]}) # to match more than one class, use a list
movies = soup.find_all("div", attrs = {"class" : "Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()

    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()

    else:
        # print(title, "Not discoutned")
        continue

    # discounted price
    price = movie.find("span", attrs= {"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    link = movie.find("a", attrs= {"class": "JC71ub"})["href"]
    # correct link : https://play.google.com + link

    print(f"Title: {title}")
    print(f"Original Price: {original_price}")
    print(f"Discounted Price: {price}")
    print("Link: ","https://play.google.com"+link)
    print("-" * 120)

browser.quit()