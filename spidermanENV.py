from asyncio.windows_events import NULL
import gym
from gym import spaces
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

def frame_forward():
    driver.find_element(By.ID,"frameforward").click()


def screenshot_game():
	el=driver.find_element(By.CSS_SELECTOR,"#gamers > ruffle-player:nth-child(1)")
	el.screenshot("game.png")
	image = cv2.imread("game.png")
	return image



# driver = webdriver.Firefox(executable_path="./geckodriver")
driver = webdriver.Firefox()
# driver.get("file:///home/rory/Desktop/Github%20repos/Spiderman-AI/spiderman.html")
driver.get("file://J:/Github%20repos/Spiderman-AI/spiderman.html")

class SpidermanENV(gym.Env):
	"""Custom Environment that follows gym interface"""

	def __init__(self, HEIGHT,WIDTH):
		super(SpidermanENV, self).__init__()
		self.reward=0
		self.height=HEIGHT
		self.width=WIDTH
		self.image=NULL
		# Define action and observation space
		# They must be gym.spaces objects
		
		# min of each action is 0, max of each is 1
		self.action_space = spaces.Box( np.array([0,0]), np.array([+1,+1]))
		# Example for using image as input (channel-first; channel-last also works):
		self.observation_space = spaces.Box(low=0, high=255,
											shape=(1, HEIGHT, WIDTH), dtype=np.uint8)

	def step(self, action):
		observation = screenshot_game()
		reward = check_reward
		done = check_over()

		return observation, reward, done, info
	def reset(self):
		...
		return observation  # reward, done, info can't be included
	def render(self, mode='human'):
		...
	def close (self):
		...