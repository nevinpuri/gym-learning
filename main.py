#!/bin/env python3
import gym
env = gym.make("LunarLander-v2")
observation, info = env.reset(return_info=True)

for i in range(1000):
    env.render()
    # action = policy(observation)
    # observation, reward, done, info = env=step(action)

    # if done:
    #     observation, info = env.reset(return_info=True)
    env.step(0)
