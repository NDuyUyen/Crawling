import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# các nhút nhấn (ENTER,...)
from selenium.webdriver.common.keys import Keys 

from time import sleep

# khai báo biến browser
s = Service('../chromedriver.exe')
browser = webdriver.Chrome(service=s)

# mở trang web, nhớ lấy permalink
browser.get("https://www.facebook.com/WarCommissar/posts/5544493558913654?__cft__[0]=AZVCDoBC9Fg8PUloM-JjjqIhmuGcaROAzDPAem4E2VJky4Z6RndNxrIqPMQn-XTBoid0pqFaJZKTGSmspk1z8mgbJeNvImBL7zEVrsVTZIMKMzaOENRu5yqdumYElaexZBzgIAy_RlDCpNMBjPUWMv2C4toNjs3gFqPf8UFrNzoSa4Y7d71i9sFYSqi-5kbTyA0&__tn__=%2CO*F")

sleep(2)

# email = browser.find_element_by_id("email")
# email.send_keys("nguyenduyuyen.enolc@gmail.com")

# password = browser.find_element_by_id("pass")
# password.send_keys("nickclonecuaUyen12321")

# sleep(2)
# password.send_keys(Keys.ENTER)


# Lấy link hiện comment
comment_click = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a")
comment_click.click()

# Lấy all comment
sleep(random.randint(1, 3))
most_rev_cmt = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div/div/div/div/a")
most_rev_cmt.click()
sleep(random.randint(1, 3))
all_cmt = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div/ul/li[3]/a/span/span/div/div[1]")
all_cmt.click()
sleep(random.randint(1, 3))
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# Load full comment
for i in range(2):
    full_cmt = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/div/a")
    
    full_cmt.click()
    sleep(2.5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
sleep(5)

cmt_list = browser.find_elements_by_xpath("//div[@aria-label='Comment']")
print(len(cmt_list))

for cmt in cmt_list:
    poster = cmt.find_element_by_class_name("_6qw4")
    content = cmt.find_element_by_class_name("_3l3x")
    print("*", poster.text, ":", content.text)

# đóng trình duyệt
browser.close()