import numpy as np

# Class to represent a sequential game for computing Subgame Perfect Equilibrium
class SequentialGame:
    def __init__(self, payoff_matrix):
        self.payoff_matrix = np.array(payoff_matrix)

    def compute_subgame_perfect_equilibrium(self):
        # Backward induction logic to find SPE
        n_stages = len(self.payoff_matrix)
        strategies = []
        for stage in reversed(range(n_stages)):
            payoffs = self.payoff_matrix[stage]
            best_response = np.argmax(payoffs)
            strategies.insert(0, best_response)
        return strategies
