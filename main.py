#!/bin/env python3
import gym
from stable_baselines3 import a2c
env = gym.make("LunarLander-v2")
observation, info = env.reset(return_info=True)

for i in range(1000):
    env.render()
    # action = policy(observation)
    # observation, reward, done, info = env=step(action)

    # if done:
    #     observation, info = env.reset(return_info=True)
    obs, reward, done, info = env.step(0)
    print(info)
