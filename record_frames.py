from ast import Str
import cv2
from cv2 import imread
from cv2 import subtract
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
import pandas as pd
import time

import re


def extract_number(f):
    s = re.findall("\d+$",f)
    return (int(s[0]) if s else -1,f)


# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
path = 'J:\Github repos\Spiderman-AI\data\myframes'
# cv2.imwrite(os.path.join(path , 'waka.jpg'), img)

# initialize the WindowCapture class
wincap = WindowCapture('Ruffle - spiderman.swf')

from datetime import datetime

bgimage = imread("game_rips/images/background.jpg")
bgimage = cv2.resize(bgimage, (110, 80))

now = datetime.now() # current date and time

import re


def extract_number(f):
    s = re.findall(r'\b\d+\b',f)
    return (int(s[0]) if s else -1,f)

from glob import iglob
# messy but this just gets the number of the largest filename in the data/myframes folder. Then the rest of the program will continue saving images from after this number
count = int(re.findall(r'\b\d+\b',max(iglob("data/myframes/*.png"),key=extract_number))[0]) + 1 or 0
# count = 0
while(True):
    time.sleep(0.07)
# # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # cropped_image = screenshot[0:360, 72:568]
    lowres_image = cv2.resize(screenshot, (110, 80))
    gray_image = cv2.cvtColor(lowres_image, cv2.COLOR_BGR2GRAY)

    subtracted = cv2.absdiff(lowres_image,bgimage)
    subtracted = cv2.cvtColor(subtracted, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(subtracted, 1, 255, cv2.THRESH_BINARY)

    cv2.imwrite(os.path.join(path , str(count)+".png"), blackAndWhiteImage)    
    count += 1
    print(count)
    # print(date_time)
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done.')
