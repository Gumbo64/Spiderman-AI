from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import numpy as np
import cv2
# import matplotlib
# from cv2 import cv
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
    
def frame_forward(n):
    for i in list(range(n)):
        driver.find_element(By.ID,"frameforward").click()


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'./Tesseract-OCR/tesseract.exe'
def screenshot_game():

    el=driver.find_element(By.CSS_SELECTOR,"#gamers > ruffle-player:nth-child(1)")
    el.screenshot("game.png")
    image = cv2.imread("game.png")





# driver = webdriver.Firefox(executable_path="./geckodriver")
driver = webdriver.Firefox()
# driver.get("file:///home/rory/Desktop/Github%20repos/Spiderman-AI/spiderman.html")
driver.get("file://J:/Github%20repos/Spiderman-AI/spiderman.html")

time.sleep(5)
click_start()
time.sleep(2)
screenshot_game()
# click_retry()
while True:
    time.sleep(0.5)
    click_coord(500,50)
    # frame_forward(5)