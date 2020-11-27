import requests
res = requests.get("http://google.com") # successful
res = requests.get("http://nadocoding.tistory.com") # erroneous

print("Response Code :", res.status_code) # if 200, accessed successfully

# if res.status_code == requests.codes.ok:    # if accessed successfully
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

res.raise_for_status()  # stops the program is the access wasn't successful
# print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)