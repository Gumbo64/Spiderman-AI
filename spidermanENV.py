# environment
import pydirectinput
import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
from gym import Env
from gym.spaces import Box, Discrete

# memory
from importlib.util import module_from_spec
from time import sleep
from pymem import *
from pymem.process import *
from memreader import get_score

# screenshots
from windowcapture import WindowCapture
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# open game
import subprocess

import win32gui
import win32con



class Spiderman_ENV(Env):
	def __init__(self):
		super().__init__()
		# Setup spaces
		
		self.window_height=800
		self.window_width=1100

		self.process_height=80
		self.process_width=110

		self.observation_space = Box(low=0, high=255, shape=(1,self.process_height,self.process_width), dtype=np.uint8)

		# 20 grid positions + none
		self.action_space = Discrete(21)


		# get all the clickable positions (a grid)
		self.action_map = []

		horizontal_split = 5
		vertical_split = 4
		
		for i in range(horizontal_split):
			x = int(i * (self.window_width / horizontal_split) + 2)
			for j in range(vertical_split):
				y = int(j * (self.window_height / vertical_split) + 2)

				self.action_map.append([x,y])




		subprocess.Popen(["ruffle.exe", "moddedspiderman.swf","--width",str(self.window_width),"--height",str(self.window_height)])
		time.sleep(3)
		self.last_score=250
		
		
		self.cap = WindowCapture('Ruffle - moddedspiderman.swf')

	def clickgame(self,x,y):
		screen_x,screen_y = self.cap.get_screen_position([x,y])
		pydirectinput.click(x=screen_x, y=screen_y)




	def step(self, action):
		if action !=20:
			coords = self.action_map[action]
			self.clickgame(coords[0], coords[1])

		
		observation = self.get_observation()
		done = self.get_done(observation) 
		reward = self.get_reward()
		info = {}
		return observation, reward, done, info
		
	
	def reset(self):
		time.sleep(0.1)
		self.mem_counter=0
		self.clickgame(540, 670)
		time.sleep(0.3)
		self.clickgame(270, 560)
		time.sleep(0.3)
		return self.get_observation()
		
	# def render(self):
	# 	cv2.imshow('Game', self.current_frame)
	# 	if cv2.waitKey(1) & 0xFF == ord('q'):
	# 		self.close()
		 
	def close(self):
		cv2.destroyAllWindows()
	
	def get_observation(self):
		# get an updated image of the game
		self.screenshot = self.cap.get_screenshot()
		
		# cropped_image = screenshot[0:360, 72:568]
		lowres_image = cv2.resize(self.screenshot, (110, 80))
		(thresh, blackAndWhiteImage) = cv2.threshold(lowres_image, 1, 255, cv2.THRESH_BINARY)
		cv2.imwrite("game.png", blackAndWhiteImage)  
		cv2.cvtColor(blackAndWhiteImage, cv2.COLOR_BGR2GRAY)
		return np.resize(blackAndWhiteImage, (1,80,110))


	def get_reward(self):
		cropped_score = self.screenshot[0:80, 0:100]
		cropped_score = cv2.inRange(cropped_score, (0), (0))
		columntotals=[]
		for column in cropped_score.T:
		#     print(column)
			columntotals.append(np.sum(column)/255)
		A = np.array([v for i, v in enumerate(columntotals) if i == 0 or v != columntotals[i-1]])
		res = A[A != 0]
		res = (res-1).tolist()
		score = int(''.join(map(str, map(int, res))))
		reward = score - self.last_score
		self.last_score=score
		return reward
	# def get_score(self):
	# 	return self.lastscore

	def get_done(self,observation):
		# print(np.sum(observation)/255)
		if np.sum(observation)/255 > 6000:
			return True
		return False
	