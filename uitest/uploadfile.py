from selenium import webdriver
import time
def uploadfile(url):
    driver = webdriver.Chrome("../drivers/chromedriver.exe")
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(6000)
    driver.find_element_by_id("userName").send_keys("moshiyong")
    driver.find_element_by_id("btnLogin").click()
    # time.sleep(10)
    driver.find_element_by_link_text("接口自动化").click()
    driver.find_element_by_link_text("接口脚本").click()
    #driver.find_element_by_link_text()
    driver.find_element_by_link_text("新增").click()
    driver.find_element_by_id("editScriptName").send_keys("红包联盟")


def getbaidu():
    driver = webdriver.Chrome("../drivers/chromedriver.exe")
    driver.get("https://www.baidu.com")
    driver.maximize_window()

uploadfile("http://dig.jdfmgt.com/index")
# getbaidu()