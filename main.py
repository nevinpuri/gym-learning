import gym
env = gym.make("LunarLander-v2")
observation, info = env.reset(seed=41, return_info=True)

k = 0

for b in range(4):
    print(b)
    for i in range(10):
        env.render()
        # action = policy(observation)
        # observation, reward, done, info = env=step(action)

        # if done:
        #     observation, info = env.reset(return_info=True)
        env.step(b)
