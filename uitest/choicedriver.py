from selenium import webdriver
import threading
import time
# def getdriver(str):
#     if str=="firefox":
#         driver=webdriver.Firefox("../drivers/geckodriver.exe");
#         return driver
#     elif str=="chrome":
#         driver=webdriver.Chrome("../drivers/chromedriver.exe");
#         return driver
#     else:
#         return

def login():
    driver = webdriver.Chrome("../drivers/chromedriver.exe")
    #driver.get("")
    driver.get("https:www.baidu.com")
    driver.maximize_window()
    driver.implicitly_wait(6000)
    #driver.find_element_by_id("username").send_keys("")
    #driver.find_element_by_id("password").send_keys("")
    timer = threading.Timer(10, login)
    timer.start()


def keyer():
    timer=threading.Timer(1,login())
    timer.start()

#keyer()
#print(time.localtime(time.time()))
def login_erp():
    driver = webdriver.Chrome("../drivers/chromedriver.exe")
    driver.get("")
    driver.maximize_window()
    driver.find_element_by_id("username").send_keys("")
    driver.find_element_by_id("password").send_keys("")
    driver.find_element_by_class_name("formsubmit_btn").click()
    driver.find_element_by_tag_name("").click()

login_erp()