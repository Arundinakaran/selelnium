from http.server import executable
from time import sleep
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.hotstar.com/in")

driver.find_element_by_id("searchField").send_keys("IPL")
driver.maximize_window()
time.sleep(10)

#pixelexprienmve