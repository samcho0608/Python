from selenium import webdriver
import time

browser = webdriver.Chrome() # rn the webdriver is already in the work space so don't need to input anything
                             # However, if it isn't we need to specify the location of the web driver
                             # e.g. webdriver.Chrome("c:/downloads/chromedriver.exe")

# 1. open the website
browser.get("https://naver.com")

# 2. click the log-in button
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. input id, pw
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. click login
browser.find_element_by_id("log.login").click()

# 5. re-input id
time.sleep(3)
# browser.find_element_by_id("id").send_keys("my_id") # doesn't work due to uncleared buffer(?)
# without clearing buffer, it'll input naver_idmy_id
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. print html info
print(browser.page_source)

# 7. terminate the browser
# browser.close() # closes just the current tab
browser.quit()