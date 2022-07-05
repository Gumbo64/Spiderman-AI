import cv2
from cv2 import imread
from cv2 import subtract
from matplotlib.pyplot import gray
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
import pickle as pk
from sklearn.decomposition import PCA
import pandas as pd
# pk.dump(faces_pca, open("pca.pkl","wb"))
myPCA = pk.load(open("pca.pkl",'rb'))


# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Ruffle - moddedspiderman.swf')

loop_time = time()

# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
 

bgimage = imread("game_rips/images/background.jpg")
bgimage = cv2.resize(bgimage, (550, 400))
# bgimage = cv2.cvtColor(bgimage, cv2.COLOR_BGR2GRAY)
    
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    #                         y, rows  x, columns
    cropped_score = screenshot[0:80, 0:100]
    cropped_score = cv2.inRange(cropped_score, (0), (0))
    columntotals=[]
    for column in cropped_score.T:
    #     print(column)
        columntotals.append(np.sum(column)/255)
    A = np.array([v for i, v in enumerate(columntotals) if i == 0 or v != columntotals[i-1]])
    res = A[A != 0]
    res = (res-1).tolist()
    res = ''.join(map(str, map(int, res)))
    print(res)
    gray_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)
    
    final_image=cv2.resize(blackAndWhiteImage, (1100, 800))
    
    # cv2.imwrite("game.png", cropped_score)    

    # cv2.imshow('PCA', final_image)
    cv2.imshow('screenshot',cropped_score)
    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done.')
