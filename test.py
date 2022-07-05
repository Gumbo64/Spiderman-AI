from spidermanENV import Spiderman_ENV
import cv2
env = Spiderman_ENV()

while True:
    cv2.imshow("a",env.render())