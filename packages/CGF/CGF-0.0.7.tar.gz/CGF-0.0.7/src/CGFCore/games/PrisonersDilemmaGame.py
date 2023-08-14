from pyrsistent import pmap
import random


class Game:
    """A generic Game class that is used to implement different types of games."""

    def __init__(
        self, payoff_matrix, transition_matrix, possible_states, actions, initial_policy
    ):
        """
        Initialize the game.

        Args:
        payoff_matrix: A nested dictionary representing the payoff for each state-action pair.
        transition_matrix: A nested dictionary representing the transition probabilities for each state-action pair.
        possible_states: A list of all possible states.
        actions: A list of all possible actions.
        initial_policy: An initial policy to start the game.
        """
        self.payoff_matrix = payoff_matrix
        self.transition_matrix = transition_matrix
        self.possible_states = possible_states
        self.actions = actions
        self.policy = pmap({state: initial_policy for state in possible_states})
        self.value_table = pmap({state: 0 for state in possible_states})

    def get_reward(self, state, action):
        """Return the reward for a given state and action."""
        return self.payoff_matrix[state][action]

    def next_state(self, state, action):
        """Return the next state given a state and action based on the transition matrix."""
        return random.choices(
            self.possible_states, weights=self.transition_matrix[state][action]
        )[0]

    def evaluate_policy(self):
        """Evaluate the current policy until convergence."""
        while True:
            delta = 0
            for state in self.possible_states:
                old_value = self.value_table[state]
                action = self.policy[state]
                new_value = (
                    self.get_reward(state, action)
                    + 0.9
                    * sum(
                        self.value_table[self.next_state(state, action)]
                        for _ in range(100)
                    )
                    / 100
                )
                delta = max(delta, abs(old_value - new_value))
                self.value_table = self.value_table.set(state, new_value)
            if delta < 0.01:
                return self.value_table

    def improve_policy(self):
        """Improve the policy based on the value table."""
        policy_stable = True
        for state in self.possible_states:
            old_action = self.policy[state]
            new_action = max(
                self.actions,
                key=lambda action: self.get_reward(state, action)
                + 0.9
                * sum(
                    self.value_table[self.next_state(state, action)] for _ in range(100)
                )
                / 100,
            )
            self.policy = self.policy.set(state, new_action)
            if old_action != new_action:
                policy_stable = False
        return policy_stable


class PrisonersDilemma(Game):
    """The Prisoner's Dilemma game class."""

    pass


class StagHunt(Game):
    """The Stag Hunt game class."""

    pass


class CompositeGame:
    """A class to combine two different games."""

    def __init__(self, game1, game2):
        """Initialize the composite game with two games."""
        self.game1 = game1
        self.game2 = game2

    def compare_value_tables(self):
        """Compare the value tables for the common states between the two games."""
        common_states = set(self.game1.possible_states).intersection(
            self.game2.possible_states
        )
        return sum(
            abs(self.game1.value_table[state] - self.game2.value_table[state])
            for state in common_states
        )

    def evaluate_policy(self):
        """Evaluate the policy for the composite game until convergence."""
        while True:
            self.game1.evaluate_policy()
            self.game2.evaluate_policy()
            if self.compare_value_tables() < 0.01:
                return

    def improve_policy(self):
        """Improve the policy for the composite game."""
        return self.game1.improve_policy() and self.game2.improve_policy()


# Initialize the games
prisoner_payoff_matrix = pmap(
    {
        "cooperate": pmap({"cooperate": 2, "defect": 0}),
        "defect": pmap({"cooperate": 3, "defect": 1}),
    }
)

stag_payoff_matrix = pmap(
    {"stag": pmap({"stag": 3, "rabbit": 0}), "rabbit": pmap({"stag": 0, "rabbit": 2})}
)

transition_matrix = {
    "cooperate": {"cooperate": [0.5, 0.5], "defect": [0.5, 0.5]},
    "defect": {"cooperate": [0.5, 0.5], "defect": [0.5, 0.5]},
    "stag": {"stag": [0.5, 0.5], "rabbit": [0.5, 0.5]},
    "rabbit": {"stag": [0.5, 0.5], "rabbit": [0.5, 0.5]},
}

prisoner_possible_states = ["cooperate", "defect"]
stag_possible_states = ["stag", "rabbit"]

prisoners_dilemma = PrisonersDilemma(
    prisoner_payoff_matrix,
    transition_matrix,
    prisoner_possible_states,
    ["cooperate", "defect"],
    "cooperate",
)
stag_hunt = StagHunt(
    stag_payoff_matrix,
    transition_matrix,
    stag_possible_states,
    ["stag", "rabbit"],
    "stag",
)

composite_game = CompositeGame(prisoners_dilemma, stag_hunt)

# Evaluate and improve the policy for each game until it converges
while True:
    composite_game.evaluate_policy()
    if composite_game.improve_policy():
        break

# Print the optimal policies and expected returns for each state
for state in composite_game.game1.possible_states:
    print(f"In the Prisoner's Dilemma game, when the current state is {state}:")
    print(f"\t- The optimal action is to {composite_game.game1.policy[state]}")
    print(f"\t- The expected return is {composite_game.game1.value_table[state]}\n")

for state in composite_game.game2.possible_states:
    print(f"In the Stag Hunt game, when the current state is {state}:")
    print(f"\t- The optimal action is to {composite_game.game2.policy[state]}")
    print(f"\t- The expected return is {composite_game.game2.value_table[state]}\n")
