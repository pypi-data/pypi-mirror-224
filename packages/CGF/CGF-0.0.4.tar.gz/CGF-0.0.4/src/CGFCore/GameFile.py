import numpy as np


class Game:
    """Base class for all types of games."""

    def __init__(self, payoff_matrix):
        self.payoff_matrix = np.array(payoff_matrix)

    def get_payoff(self, actions):
        """Returns the payoff given a list of actions."""
        return self.payoff_matrix[tuple(actions)]
