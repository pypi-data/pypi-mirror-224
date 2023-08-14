import time
import matplotlib.pyplot as plt
import numpy as np

class OpenGame:
    def __init__(self, players):
        self.players = players
        self.strategies = {player: None for player in players}
        self.history = []
        self.future = []

    def set_strategy(self, player, strategy):
        self.strategies[player] = strategy

    def play(self, history):
        raise NotImplementedError("Each game must implement its own play function.")

    def coplay(self, future, outcome):
        raise NotImplementedError("Each game must implement its own coplay function.")

    def utility(self, history, future, outcome, player):
        raise NotImplementedError("Each game must implement its own utility function.")

class PrisonersDilemma(OpenGame):
    def __init__(self, agents):
        player_names = [f"player{i+1}" for i in range(len(agents))]
        super().__init__(player_names)
        self.agents = agents
        self.payoffs = {
            ("cooperate", "cooperate"): {player: 2 for player in player_names},
            ("cooperate", "defect"): {player: 0 if player == "player1" else 3 for player in player_names},
            ("defect", "cooperate"): {player: 3 if player == "player1" else 0 for player in player_names},
            ("defect", "defect"): {player: 1 for player in player_names}
        }

    def play(self, history):
        state = tuple(history)
        actions = [agent.choose_action(state) for agent in self.agents]
        return tuple(actions)

    def coplay(self, future, outcome):
        return future

    def feedback(self, outcome):
        rewards = [self.payoffs[outcome][player] for player in self.players]
        return rewards

    def utility(self, history, future, outcome, player):
        return self.payoffs[outcome][player]

class CompositeOpenGame(OpenGame):
    def __init__(self, game1, game2, composition_type="sequential"):
        super().__init__(game1.players + game2.players)
        self.game1 = game1
        self.game2 = game2
        self.composition_type = composition_type

    def play(self, history):
        if np.random.rand() > 0.5:
           self.composition_type = "sequential"
        else:
           self.composition_type = "parallel"
        if self.composition_type == "sequential":
            outcome1 = self.game1.play(history)
            outcome2 = self.game2.play(history + [outcome1])
            return outcome1, outcome2
        elif self.composition_type == "parallel":
            outcome1 = self.game1.play(history)
            outcome2 = self.game2.play(history)
            return outcome1, outcome2
        else:
            raise ValueError("Invalid composition type")

    def coplay(self, future, outcome):
        future1, future2 = future
        outcome1, outcome2 = outcome
        coplayed_future1 = self.game1.coplay(future1, outcome1)
        coplayed_future2 = self.game2.coplay(future2, outcome2)
        return coplayed_future1, coplayed_future2

    def utility(self, history, future, outcome, player):
        outcome1, outcome2 = outcome
        if player in self.game1.players:
            coplayed_future1, _ = self.coplay(future, outcome)
            return self.game1.utility(history, coplayed_future1, outcome1, player)
        elif player in self.game2.players:
             _, coplayed_future2 = self.coplay(future, outcome)
             return self.game2.utility(history, coplayed_future2, outcome2, player)
        else:
             raise ValueError(f"{player} is not a player in this composite game")

class RLAgent:
    def __init__(self, actions):
        self.actions = actions
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.1

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.choice(self.actions)
        q_values = [self.get_q_value(state, action) for action in self.actions]
        return self.actions[np.argmax(q_values)]

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0)

    def learn(self, state, action, reward, next_state):
        predict = self.get_q_value(state, action)
        target = reward + self.discount_factor * np.max([self.get_q_value(next_state, next_action) for next_action in self.actions])
        self.q_table[(state, action)] = predict + self.learning_rate * (target - predict)
        self.learning_rate = 0.1 + np.random.normal(0, 0.01)


def train_rl_agents(episodes=None):
    if not episodes:
        episodes = 1000 + np.random.randint(-100, 100)
    agents = [RLAgent(actions=["cooperate", "defect"]) for _ in range(2)]
    game = PrisonersDilemma(agents)
    rewards_over_time = []  # Store average rewards for each episode

    action_counts = {"cooperate": 0, "defect": 0}

    for episode in range(episodes):
        history = ["previous_play"]
        outcome = game.play(history)
        rewards = game.feedback(outcome)
        avg_reward = np.mean(rewards)  # Calculate average reward for the episode
        rewards_over_time.append(avg_reward)  # Append to the list

        for agent, reward in zip(agents, rewards):
            state = tuple(history)
            action = agent.choose_action(state)
            action_counts[action] += 1
            next_history = history + list(outcome)
            next_state = tuple(next_history)
            agent.learn(state, action, reward, next_state)
            history = next_history
    return agents, rewards_over_time, action_counts


trained_agents, rewards_over_time, action_counts = train_rl_agents()

# Define the state transition probabilities
def transition_prob(current_state, action1, action2):
    if current_state[1:] == (action1, action2):
        return 1
    return 0

# Define the reward function
def reward(state, player, game):
    return game.payoffs[state[1:]][player]

def value_iteration(game, states, actions, theta=1e-6, discount_factor=0.9):
    V = {state: 0 for state in states}
    while True:
        delta = 0
        for state in states:
            v = V[state]
            V[state] = max(sum(transition_prob(state, action1, action2) * (reward(state, "player1", game) + discount_factor * V[state])
                               for action2 in actions) for action1 in actions)
            delta = max(delta, abs(v - V[state]))
        if delta < theta:
            break

    # Extract policy
    policy = {}
    for state in states:
        best_action_value = float('-inf')
        best_action = None
        for action in actions:
            action_value = sum(transition_prob(state, action, action2) * (reward(state, "player1", game) + discount_factor * V[state])
                               for action2 in actions)
            if action_value > best_action_value:
                best_action_value = action_value
                best_action = action
        policy[state] = best_action

    return V, policy

# Testing functions
def test_open_games(agents):
    game = PrisonersDilemma(agents)
    history = ["previous_play"]
    outcome = game.play(history)
    future = game.coplay(["potential_future"], outcome)
    utilities = {player: game.utility(history, future, outcome, player) for player in game.players}
    print(f"Outcome: {outcome}")
    print(f"Utilities: {utilities}")

def test_composite_open_games(agents1, agents2):
    game1 = PrisonersDilemma(agents1)
    game2 = PrisonersDilemma(agents2)
    composite_game = CompositeOpenGame(game1, game2, "parallel")
    history = ["previous_play"]
    outcome = composite_game.play(history)
    future = composite_game.coplay(["potential_future1", "potential_future2"], outcome)
    utilities = {player: composite_game.utility(history, future, outcome, player) for player in composite_game.players}
    print(f"Outcome: {outcome}")
    print(f"Utilities: {utilities}")

# Plotting functions
def plot_rewards(rewards_over_time):
    plt.figure()
    plt.plot(rewards_over_time)
    plt.xlabel('Episode')
    plt.ylabel('Average Reward')
    plt.title('Average Reward per Episode')
    plt.tight_layout()
    plt.show()

def plot_action_counts(action_counts):
    plt.figure()
    actions = list(action_counts.keys())
    counts = list(action_counts.values())
    plt.bar(actions, counts)
    plt.xlabel('Action')
    plt.ylabel('Count')
    plt.title('Action Distribution')
    plt.tight_layout()
    plt.show()

# Let's test the modifications
agents = [RLAgent(actions=["cooperate", "defect"]) for _ in range(2)]
test_open_games(agents)
test_composite_open_games(agents, agents)
plot_rewards(rewards_over_time)
plot_action_counts(action_counts)

