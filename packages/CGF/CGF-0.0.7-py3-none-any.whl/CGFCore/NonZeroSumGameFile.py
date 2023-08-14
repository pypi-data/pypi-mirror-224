import numpy as np

from CGFCore.GameFile import Game


class NonZeroSumGame(Game):
    """Represents a non-zero sum game."""

    def __init__(self, payoff_matrix):
        # Constructor of the NonZeroSumGame class. It takes a payoff_matrix as an argument.
        super().__init__(payoff_matrix)
        # Calls the constructor of the superclass Game, passing the payoff_matrix as an argument.
        # This line allows NonZeroSumGame to inherit the attributes and methods of the superclass Game.
        self.players = len(payoff_matrix)
        # initializes the number of players in the game to be the number of elements in the list payoff_matrix

    def best_response(self, player, opponent_strategy):
        # calculates the best response for a given player against a given opponent strategy.
        expected_payoffs = np.dot(self.payoff_matrix[player], opponent_strategy)
        # calculates the expected payoffs for each strategy of the player by dot product of the player's row of the payoff matrix and the opponent's strategy vector.
        best_response = np.argmax(expected_payoffs)
        # calculates the best response strategy of the player, which is the strategy that gives the maximum expected payoff.
        return best_response

    def compute_nash_equilibrium(self, initial_strategies, iterations=1000):
        # computes an approximation of the Nash Equilibrium of the game using a simple iterative method.
        # It takes as input initial_strategies which is a list of initial strategies for each player and iterations which is the number of iterations to run the algorithm.
        # If iterations is not provided, it defaults to 1000.
        strategies = initial_strategies
        for _ in range(iterations):
            for player in range(self.players):
                opponent = 1 - player  # This works for 2-player games.
                strategies[player] = self.best_response(player, strategies[opponent])
                # This line updates the strategy of the current player to be the best response against the current strategy of the opponent player.
        return strategies
