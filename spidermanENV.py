# environment
from click import option
import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
from gym import Env
from gym.spaces import Box, Discrete


from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# screenshots
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)



class Spiderman_ENV(Env):
	def __init__(self,headless):
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




		options = FirefoxOptions()
		if headless==True:
			options.add_argument("--headless")
		self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)

		# self.driver = webdriver.Chrome('./chromedriver')

		self.driver.set_window_size(1200, 1000)
		# driver.get("file:///home/rory/Desktop/Github%20repos/Spiderman-AI/spiderman.html")
		self.driver.get("file://J:/Github%20repos/Spiderman-AI/spiderman.html")
		

		time.sleep(10)
		self.last_score=295


	def clickgame(self,x,y):
		el=self.driver.find_element(By.TAG_NAME,"body")
		action = webdriver.common.action_chains.ActionChains(self.driver)


		# selenium had a weird offset
		action.move_to_element_with_offset(el, x-594, y-412)
		action.click()
		action.perform()




	def step(self, action):
		if action !=20:
			coords = self.action_map[action]
			self.clickgame(coords[0], coords[1])

		
		observation = self.get_observation()
		done = self.get_done(observation) 
		reward = self.get_reward()
		# print(reward)
		info = {}
		return observation, reward, done, info
		
	
	def reset(self):
		time.sleep(0.1)
		self.clickgame(540, 670)
		time.sleep(0.3)
		self.clickgame(270, 560)
		time.sleep(0.3)
		self.last_score=295
		return self.get_observation()
		
	# def render(self):
	# 	cv2.imshow('Game', self.current_frame)
	# 	if cv2.waitKey(1) & 0xFF == ord('q'):
	# 		self.close()
		 
	def close(self):
		self.driver.close()
		self.driver.quit()
		print('im dead')
	
	def game_screenshot(self):
		el=self.driver.find_element(By.CSS_SELECTOR,"#gamers > ruffle-player:nth-child(1)")
		el.screenshot("screenshot.png")
		return cv2.imread("screenshot.png")

	def get_observation(self):
		# get an updated image of the game
		self.screenshot = self.game_screenshot()
		
		# cropped_image = screenshot[0:360, 72:568]
		lowres_image = cv2.resize(self.screenshot, (110, 80))
		greyscale_image = cv2.cvtColor(lowres_image, cv2.COLOR_BGR2GRAY)
		(thresh, blackAndWhiteImage) = cv2.threshold(greyscale_image, 1, 255, cv2.THRESH_BINARY)
		# cv2.imwrite("game.png", blackAndWhiteImage)  
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
		reward = max(score - self.last_score,0)
		self.last_score=score
		# print(reward)
		return reward
	# def get_score(self):
	# 	return self.lastscore

	def get_done(self,observation):
		# print(np.sum(observation)/255)
		if np.sum(observation)/255 > 6000:
			return True
		return False
	

if __name__ == "__main__":
	env = Spiderman_ENV()
	# print('starting wait')
	# time.sleep(2)
	print('wait done')
	env.reset()
	# while True:
	# 	env.clickgame(540,670)
	# 	time.sleep(1)
