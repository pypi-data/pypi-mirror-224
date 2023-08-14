# 5
import numpy as np


class MDP:
    def __init__(self, num_states, num_actions, transition_matrix, reward_matrix):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_matrix = transition_matrix
        self.reward_matrix = reward_matrix


class SARSA:
    def __init__(
        self, mdp, value_function, learning_rate=0.1, discount_factor=0.9, epsilon=0.1
    ):
        self.mdp = mdp
        self.value_function = value_function
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon

    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.mdp.num_actions)
        else:
            return np.argmax(self.value_function[state])

    def update_value_function(self, state, action, reward, next_state, next_action):
        current_value = self.value_function[state]
        next_value = self.value_function[next_state]

        td_error = reward + self.discount_factor * next_value - current_value
        self.value_function[state] += self.learning_rate * td_error


class ValueFunction:
    def __init__(self, num_states):
        self.num_states = num_states
        self.values = np.zeros(num_states)

    def __getitem__(self, state):
        return self.values[state]

    def __setitem__(self, state, value):
        self.values[state] = value


# Example usage

num_states = 10
num_actions = 4

transition_matrix = np.random.rand(num_states, num_actions, num_states)
transition_matrix = transition_matrix / transition_matrix.sum(axis=2, keepdims=True)
reward_matrix = np.random.rand(num_states)

mdp = MDP(num_states, num_actions, transition_matrix, reward_matrix)
value_function = ValueFunction(num_states)
sarsa = SARSA(mdp, value_function)


num_episodes = 1000
for _ in range(num_episodes):
    state = 0
    action = sarsa.get_action(state)

    while True:
        next_state = np.random.choice(
            range(num_states), p=mdp.transition_matrix[state, action]
        )
        next_action = sarsa.get_action(next_state)
        reward = mdp.reward_matrix[state]

        sarsa.update_value_function(state, action, reward, next_state, next_action)

        state = next_state
        action = next_action

        if state == num_states - 1:
            break

# Access the learned value function
value_function = sarsa.value_function
print("Learned Value Function:")
print(value_function)
print("Learned Value Function:")
print(value_function.values)
