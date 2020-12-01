from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 27, 28일 선택
# browser.find_elements_by_link_text("27")[0].click()
# browser.find_elements_by_link_text("28")[0].click()

# 다음 달 27, 28일 전택
browser.find_elements_by_link_text("27")[1].click()
browser.find_elements_by_link_text("28")[1].click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색
browser.find_element_by_link_text("항공권 검색").click()

# how to deal with loading
try:
    elem = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # wait for 10 sec max until the condition is satisfied
    # in this case the until the element with the given XPATH is found
    # after 10 sec, raises error
    print(elem.text)
except:
    # if not found in 10 sec, just quit the browser
    browser.quit()

# print result
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)