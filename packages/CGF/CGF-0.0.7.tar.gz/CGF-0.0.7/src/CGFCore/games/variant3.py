# 3
import random
import numpy as np

# Define the payoffs
prisoner_payoff = {
    ("cooperate", "cooperate"): {"cooperate": 2, "defect": 0},
    ("cooperate", "defect"): {"cooperate": -1, "defect": -1},
    ("defect", "cooperate"): {"cooperate": 3, "defect": 1},
    ("defect", "defect"): {"cooperate": 0, "defect": 0},
}

# Define the initial value table and policy
value_table = {}
policy = {}

# Define the states
states = [
    ("cooperate", "cooperate"),
    ("cooperate", "defect"),
    ("defect", "cooperate"),
    ("defect", "defect"),
]

# Initialize the policy and value table
for state in states:
    policy[state] = random.choice(["cooperate", "defect"])
    value_table[state] = 0

# Discount factor
gamma = 0.9

# Policy iteration
for _ in range(1000):
    # Policy evaluation
    while True:
        delta = 0
        for state in states:
            v = value_table[state]
            action = policy[state]
            value_table[state] = sum(
                [
                    prisoner_payoff[next_state][action]
                    + gamma * value_table[next_state]
                    for next_state in states
                ]
            ) / len(states)
            delta = max(delta, abs(v - value_table[state]))
        if delta < 0.01:
            break

    # Policy improvement
    policy_stable = True
    for state in states:
        old_action = policy[state]
        policy[state] = max(
            ["cooperate", "defect"],
            key=lambda action: sum(
                [
                    prisoner_payoff[next_state][action]
                    + gamma * value_table[next_state]
                    for next_state in states
                ]
            )
            / len(states),
        )
        if old_action != policy[state]:
            policy_stable = False

    if policy_stable:
        break

# Print the final policy and value table
print("Final Policy:", policy)
print("Final Value Table:", value_table)
