import requests, os
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find("ol", attrs={"class":"type_plural list_exact movie_list"}).find_all("img", attrs={"class":"thumb_img"})

for i, image in enumerate(images):
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:" + image_url

    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open(os.path.dirname(__file__)+"/imgdnld/movie{}.jpg".format(i+1), "wb") as f:
        f.write(image_res.content)
