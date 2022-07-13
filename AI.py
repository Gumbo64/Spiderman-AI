#!/usr/bin/env python
# coding: utf-8

# # 3. Train the Model

# In[1]:


# %load_ext tensorboard


# In[2]:


# %tensorboard --logdir logs


# In[3]:


# %tensorboard --logdir logs


# In[4]:


# pip install pyqt5 --user


# ## 3.1 Create Callback

# In[5]:


# Import os for file path management
import os 
# Import Base Callback for saving models
from stable_baselines3.common.callbacks import BaseCallback
# Check Environment    
from stable_baselines3.common import env_checker


# In[6]:


class TrainAndLoggingCallback(BaseCallback):

    def __init__(self, check_freq, save_path, verbose=1):
        super(TrainAndLoggingCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.save_path = save_path

    def _init_callback(self):
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self):
        if self.n_calls % self.check_freq == 0:
            model_path = os.path.join(self.save_path, 'best_model_{}'.format(self.n_calls))
            self.model.save(model_path)

        return True


# In[7]:


CHECKPOINT_DIR = './train/'
LOG_DIR = './logs/'


# In[8]:


callback = TrainAndLoggingCallback(check_freq=10000, save_path=CHECKPOINT_DIR)


# ## 3.2 Build DQN and Train

# In[9]:

import time
from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack


# In[10]:


from spidermanENV import Spiderman_ENV
env = Spiderman_ENV()


# In[11]:


# from matplotlib import pyplot as plt
# import cv2
# while True:
#     plt.imshow(env.get_observation())


# In[12]:


model = DQN('CnnPolicy', env, tensorboard_log=LOG_DIR, verbose=1, buffer_size=500000, learning_starts=5000)

# because we've already trained it past the first 5000, learning start at 0
# model = DQN('CnnPolicy', env, tensorboard_log=LOG_DIR, verbose=1, buffer_size=500000, learning_starts=0)
# model.load('train/the_best_model_160000') 


# In[13]:

try:
    model.learn(total_timesteps=1000000, callback=callback)
except KeyboardInterrupt:
    print('Caught')
    env.close()
    quit()
print('wtf')
# In[ ]:


model.load('train_first/best_mode l_50000') 


# In[ ]:





# # 4. Test out Model

# In[ ]:


for episode in range(5): 
    obs = env.reset()
    done = False
    total_reward = 0
    while not done: 
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(int(action))
        time.sleep(0.01)
        total_reward += reward
    print('Total Reward for episode {} is {}'.format(episode, total_reward))
    time.sleep(2)


# In[ ]:





# In[ ]:





# In[ ]:




