from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# các nhút nhấn (ENTER,...)
from selenium.webdriver.common.keys import Keys 

from time import sleep

# khai báo biến browser
s = Service('../chromedriver.exe')
browser = webdriver.Chrome(service=s)

# mở trang web
browser.get("https://facebook.com")

email = browser.find_element_by_id("email")
email.send_keys("12234")

password = browser.find_element_by_id("pass")
password.send_keys("12234")

password.send_keys(Keys.ENTER)


sleep(8)

# đóng trình duyệt
browser.close()