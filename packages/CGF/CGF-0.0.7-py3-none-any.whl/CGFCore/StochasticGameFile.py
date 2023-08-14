import numpy as np


class StochasticGame:
    """Base class for stochastic games."""

    # Stochastic games are a type of dynamic game where the game evolves over time according to some probabilities which are influenced by the actions of the players.
    def __init__(self, transition_matrix, payoff_matrix, discount_factor=1):
        self.transition_matrix = np.array(transition_matrix)
        self.payoff_matrix = np.array(payoff_matrix)
        self.discount_factor = discount_factor
        self.state = 0  # Initial state

    def transition(self, actions):
        """Transition to the next state given a list of actions."""
        self.state = np.random.choice(
            len(self.transition_matrix),
            p=self.transition_matrix[self.state][tuple(actions)],
        )

    def get_payoff(self, actions):
        """Returns the payoff given a list of actions."""
        return self.payoff_matrix[self.state][tuple(actions)]

    def compute_markov_perfect_equilibrium(self, iterations=1000):
        num_actions = self.payoff_matrix.shape[1:]
        num_states = self.payoff_matrix.shape[0]

        # Initial guess for value function
        value = np.zeros(num_states)

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
