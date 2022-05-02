from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://www.rvce.edu.in/")
driver.maximize_window()
time.sleep(3)

driver.find_element(by=By.LINK_TEXT, value="Departments").click()
time.sleep(3)
driver.find_element(by=By.XPATH, value="//a[contains(text(),'Master of Computer Applications')]").click()
time.sleep(3)
driver.find_element(by=By.XPATH, value="//a[contains(text(),'Scheme and Syllabus')]").click()
time.sleep(3)
driver.find_element(by=By.XPATH, value="//a[contains(text(),'MCA Handbook 2021')]").click()

