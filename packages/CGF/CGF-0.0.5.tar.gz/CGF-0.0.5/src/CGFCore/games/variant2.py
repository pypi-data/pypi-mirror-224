# 2
from lenses import lens
from copy import deepcopy
import random

# Strategy definitions
def adaptive_strategy(state, value_table, possible_actions):
    current_best_action = None
    current_best_value = float('-inf')

    for action in possible_actions:
        value = value_table.get((state, action), 0)
        if value > current_best_value:
            current_best_action = action
            current_best_value = value

    return current_best_action

# Payoff matrix
prisoner_payoff = {
    'cooperate': {'cooperate': 1, 'defect': -1},
    'defect': {'cooperate': 2, 'defect': -2}
}

stag_payoff = {
    'stag': {'stag': 3, 'rabbit': 0},
    'rabbit': {'stag': 0, 'rabbit': 1}
}

# Game play functions
def play_game(players, value_table, game):
    for player in players:
        state = (player[game + '_state'], players[1 - player['id']][game + '_state'])
        action = player['strategy'](state, value_table, ['cooperate', 'defect'] if game == 'prisoner' else ['stag', 'rabbit'])
        if game == 'prisoner':
            payoff = prisoner_payoff[action][players[1 - player['id']][game + '_action']]
        else:
            payoff = stag_payoff[action][players[1 - player['id']][game + '_action']] if random.choice([True, False]) or action == 'rabbit' else 0
        players = lens[player['id']][game + '_action'].set(action)(players)
        players = lens[player['id']]['score'].modify(lambda s: s + payoff)(players)
        players = lens[player['id']][game + '_state'].set((player[game + '_action'], players[1 - player['id']][game + '_action']))(players)

    return players

# Players
players = [
    {'name': 'player1', 'id': 0, 'strategy': adaptive_strategy, 'prisoner_state': ('none', 'none'), 'stag_state': ('none', 'none'), 'prisoner_action': 'cooperate', 'stag_action': 'stag', 'score': 0},
    {'name': 'player2', 'id': 1, 'strategy': adaptive_strategy, 'prisoner_state': ('none', 'none'), 'stag_state': ('none', 'none'), 'prisoner_action': 'cooperate', 'stag_action': 'stag', 'score': 0}
]

value_table = {}

# Play the game for 100 rounds
for _ in range(100):
    players = deepcopy(players)
    players = play_game(players, value_table, 'prisoner')
    players = play_game(players, value_table, 'stag')

    for player in players:
        for game in ['prisoner', 'stag']:
            state = (player[game + '_state'], player[game + '_action'])
future_value = max(value_table.get((state, action), 0) for action in (['cooperate', 'defect'] if game == 'prisoner' else ['stag', 'rabbit']))
value_table[(state, player[game + '_action'])] = (
    prisoner_payoff[player[game + '_action']][players[1 - player['id']][game + '_action']] + 0.9 * future_value
    if game == 'prisoner'
    else (
        stag_payoff[player[game + '_action']][players[1 - player['id']][game + '_action']]
        if random.choice([True, False]) or player[game + '_action'] == 'rabbit'
        else 0
    )
    + 0.9 * future_value
)



# Print the final states and value table
for player in players:
    print(player)
print(value_table)


for key, value in value_table.items():
    print(f"In the state {key[0]}, the value of action {key[1]} is {value}")
