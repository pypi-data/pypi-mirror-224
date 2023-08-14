import numpy as np

# Class to represent a Bayesian game for computing Bayesian Nash Equilibrium
class BayesianGame:
    def __init__(self, type_payoff_matrix, beliefs):
        self.type_payoff_matrix = np.array(
            type_payoff_matrix
        )  # Payoffs for different types
        self.beliefs = np.array(beliefs)  # Beliefs about other players' types

    def compute_bayesian_nash_equilibrium(self):
        strategies = []
        for player in range(len(self.beliefs)):
            player_belief = self.beliefs[player]
            expected_payoffs = np.dot(self.type_payoff_matrix[player], player_belief)
            best_response = np.argmax(expected_payoffs)
            strategies.append(best_response)
        return strategies
