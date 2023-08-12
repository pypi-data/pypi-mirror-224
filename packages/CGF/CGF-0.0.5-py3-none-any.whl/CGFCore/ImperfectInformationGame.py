import numpy as np
from CGFCore.StochasticGameFile import StochasticGame


class ImperfectInformationGame(StochasticGame):
    """Represents a stochastic game with imperfect information."""

    def __init__(
        self, transition_matrix, payoff_matrix, signal_matrix, discount_factor=1
    ):
        super().__init__(transition_matrix, payoff_matrix, discount_factor)
        self.signal_matrix = np.array(
            signal_matrix
        )  # Probability distribution over signals for each state

    def get_signal(self):
        """Returns a noisy signal about the state of the game."""
        return np.random.choice(
            len(self.signal_matrix), p=self.signal_matrix[self.state]
        )

    def compute_markov_perfect_equilibrium(self, iterations=1000):
        num_actions = self.payoff_matrix.shape[1:]
        num_states = self.payoff_matrix.shape[0]
        num_signals = self.signal_matrix.shape[1]

        # Initial guess for value function
        value = np.zeros((num_states, num_states))  # value for each belief state

        for _ in range(iterations):
            # Compute expected continuation values
            expected_continuation_value = self.discount_factor * np.tensordot(
                self.transition_matrix, value, axes=1
            )

            # Compute expected payoffs
            expected_payoff = np.tensordot(
                self.payoff_matrix + expected_continuation_value,
                np.ones(num_actions),
                axes=1,
            )

            # Best response given the value function
            best_response = np.argmax(expected_payoff, axis=-1)

            # Compute new values
            new_value = np.choose(best_response, expected_payoff.T)

            # Check for convergence
            if np.allclose(new_value, value):
                break

            value = new_value

        return value, best_response
