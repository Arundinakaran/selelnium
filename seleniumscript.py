from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="./chromedriver")
#driver.maxi
browser.get('https://www.rvce.edu.in')
print('Title: %s' % browser.title)
time.sleep(10)
browser.find_element_by_link_text(Departments).click()

#browser.quit()
