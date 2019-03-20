from selenium import webdriver
from time import sleep

mobileEmulation = {'deviceName': 'Apple iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe', chrome_options=options)
driver.get('')

sleep(3)