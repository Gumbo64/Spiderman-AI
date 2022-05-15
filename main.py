from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("J:\Github repos\Spiderman-AI\spiderman.html")
time.sleep(1000)
el=driver.find_elements_by_xpath("/div/canvas")[0]


while True:
    time.sleep(1000)
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, 100, 100)
    action.click()
    action.perform()