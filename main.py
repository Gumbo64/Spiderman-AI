from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# print(dir_path)

def click_coord(x,y):
    el=driver.find_element(By.ID,"bigbody")
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, x, y)
    action.click()
    action.perform()

def click_start():
    click_coord(130,280)

def click_retry():
    click_coord(194,335)


driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get("file:///home/rory/Desktop/Github%20repos/Spiderman-AI/spiderman.html")
time.sleep(5)
click_start()
time.sleep(20)
click_retry()
while True:
    time.sleep(0.5)