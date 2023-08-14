# 4
import gym
from gym import spaces
import numpy as np


class CustomGameEnv(gym.Env):
    def __init__(self):
        super(CustomGameEnv, self).__init__()
        # Action space 'cooperate', 'defect', 'stag', 'rabbit'
        self.action_space = spaces.Discrete(4)
        # State space - binary representing each game's state
        self.observation_space = spaces.Box(low=0, high=1, shape=(2,), dtype=np.uint8)

        # Payoff matrices
        self.prisoner_payoff_matrix = {
            "cooperate": {"cooperate": 2, "defect": 0},
            "defect": {"cooperate": 3, "defect": 1},
        }
        self.stag_payoff_matrix = {
            "stag": {"stag": 3, "rabbit": 0},
            "rabbit": {"stag": 0, "rabbit": 2},
        }
        self.state = None

    def step(self, action):
        if action == 0:  # cooperate
            reward = self.prisoner_payoff_matrix["cooperate"]["cooperate"]
            self.state = 0
        elif action == 1:  # defect
            reward = self.prisoner_payoff_matrix["defect"]["defect"]
            self.state = 1
        elif action == 2:  # stag
            reward = self.stag_payoff_matrix["stag"]["stag"]
            self.state = 0
        else:  # rabbit
            reward = self.stag_payoff_matrix["rabbit"]["rabbit"]
            self.state = 1
        done = True
        return np.array([self.state]), reward, done, {}

    def reset(self):
        self.state = 0
        return np.array([self.state])


from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

env = DummyVecEnv([lambda: CustomGameEnv()])
model1 = PPO("MlpPolicy", env, verbose=1)
model2 = PPO("MlpPolicy", env, verbose=1)

# Train the agents
model1.learn(total_timesteps=10000)
model2.learn(total_timesteps=10000)

observation = env.reset()  # Get an initial observation
action, _ = model1.predict(observation)  # Have the model choose an action
