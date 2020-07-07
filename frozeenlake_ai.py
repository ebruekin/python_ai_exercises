# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:53:13 2020

@author: Perona
"""

import gym
import numpy as np
import random
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v0')

### makes environment deterministic
from gym.envs.registration import register
register(
    id='FrozenLakeNotSlippery-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery': False},
    max_episode_steps=100,
    reward_threshold=0.78, # optimum = .8196
)

# Q table
q_table = np.zeros([env.observation_space.n, env.action_space.n])
#hyperparameter

gamma =0.9
alpha = 0.8
epsilon= 0.1

#☺plotting metrix 
reward_list = []

episode = 100000
for i in range(episode):
    #initiliazed environment
    state = env.reset()
    reward_count = 0
    while True:
        #exploid vs explore to find action
        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])
            
        #action process and tajke reward,next state
        
        next_state,reward,done,_=env.step(action)
        
        #q learning function
        old_value = q_table[state,action]
        next_max = np.max(q_table[next_state])
        next_value = (1-alpha) * old_value + alpha *(reward + gamma*next_max)
        
        #q table update
        
        q_table[state,action] = next_value
        
        #update state
        
        state =next_state
        
        reward_count += reward
        
    
        
        if done:
            break
        
    if i%10 ==0:
        
        reward_list.append(reward_count)
        print("Episode: {}, reward {}".format(i,reward_count))
        
        
        
plt.plot(reward_list)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        







