from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def click_coord(x,y):
    el=driver.find_element(By.ID,"bigbody")
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, x, y)
    action.click()
    action.perform()



driver = webdriver.Firefox()
driver.get("J:\Github repos\Spiderman-AI\spiderman.html")
time.sleep(5)
click_coord(130,280)

while True:

    time.sleep(0.5)