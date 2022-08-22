#!/usr/bin/python3.10

import gym
env = gym.make("LunarLander-v2")
observation, info = env.reset(seed=42, return_info=True)

for _ in range(1000):
    env.render()
    observation, reward, done, info = env.step(1)

    if done:
        observation, info = env.reset(return_info=True)

env.close()
