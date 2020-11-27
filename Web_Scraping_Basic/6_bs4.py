# beautifulsoup4 library for web scraping
# lxml library is for parsing
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())

# print(soup.a) # soup.a is the very first a tag element info on the url

# print(soup.a.attrs) # prints out the dictionary of all attribute values of the first a tag
# print(soup.a["href"]) # print out the href attribute's value of the first a tag

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # find the first a tag whose class attribute value is Nbtn_upload
# print(soup.find(attrs={"class":"Nbtn_upload"})) # find the first element whose class attribute value is Nbtn_upload
# print(soup.find("li", attrs={"class" : "rank01"}))
# rank1 = soup.find("li", attrs={"class" : "rank01"})
# print(rank1.a) # print out only the first a tag value

# SIBLINGS
# print(rank1.next_sibling) # was empty(prolly cuz there's a forced line change)
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling

# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling

# print(rank2.a.get_text())

# rank2 = rank1.find_next_sibling("li") # find the next sibling that is a li tag
# print(rank2.a.get_text())

# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# ranks_after_1 = rank1.find_next_siblings("li") # find all siblings that are li tag
# print([rank.a.get_text() for rank in ranks_after_1])

# PARENTS

# print(rank1.parent)

webtoon = soup.find("a", text="이두나!-67화. 초콜릿과 바나나와 산호") 
# from the website, find the a tag with its text as 이두나!-67화. 초콜릿과 바나나와 산호
print(webtoon.get_text())