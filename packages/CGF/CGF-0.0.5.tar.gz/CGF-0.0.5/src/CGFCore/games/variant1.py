# 1
from lenses import lens
import numpy as np
from copy import deepcopy

# Strategy definitions
def tit_for_tat(history, default):
    if not history:
        return default
    return history[-1]


def random_choice_stag(history, default):
    return np.random.choice(["stag", "rabbit"])


def random_choice_prisoner(history, default):
    return np.random.choice(["cooperate", "defect"])


# Payoff matrix
prisoner_payoff = {
    "cooperate": {"cooperate": 1, "defect": -1},
    "defect": {"cooperate": 2, "defect": -2},
}

# New payoff matrix for different weather conditions
stag_payoff = {
    "good": {"stag": {"stag": 3, "rabbit": 0}, "rabbit": {"stag": 0, "rabbit": 1}},
    "bad": {"stag": {"stag": 1, "rabbit": 0}, "rabbit": {"stag": 0, "rabbit": 0.5}},
}

# Game play functions
def play_prisoner_game(players):
    for i in range(2):
        history = players[i]["prisoner_history"]
        action = players[i]["strategy"](players[1 - i]["prisoner_history"], "cooperate")
        new_history = history + [action]
        players = lens[i]["prisoner_history"].set(new_history)(players)
        players = lens[i]["score"].modify(
            lambda s: s
            + prisoner_payoff[action][
                players[1 - i]["prisoner_history"][-1]
                if players[1 - i]["prisoner_history"]
                else "cooperate"
            ]
        )(players)
    return players


# New game play function with random weather
def play_stag_game(players):
    weather = np.random.choice(["good", "bad"])  # Randomly select the weather
    for i in range(2):
        history = players[i]["stag_history"]
        action = players[i]["stag_strategy"](players[1 - i]["stag_history"], "stag")
        new_history = history + [action]
        players = lens[i]["stag_history"].set(new_history)(players)
        players = lens[i]["score"].modify(
            lambda s: s
            + stag_payoff[weather][action][
                players[1 - i]["stag_history"][-1]
                if players[1 - i]["stag_history"]
                else "rabbit"
            ]
        )(players)
    return players


def play_game(players):
    players = play_prisoner_game(players)
    players = play_stag_game(players)
    return players


# Players
players = [
    {
        "name": "player1",
        "strategy": tit_for_tat,
        "stag_strategy": tit_for_tat,
        "prisoner_history": [],
        "stag_history": [],
        "score": 0,
    },
    {
        "name": "player2",
        "strategy": random_choice_prisoner,
        "stag_strategy": random_choice_stag,
        "prisoner_history": [],
        "stag_history": [],
        "score": 0,
    },
]

# Play the game for 10 rounds
for _ in range(10):
    players = play_game(deepcopy(players))

# Print the final states
for player in players:
    print(player)
