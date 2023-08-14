import numpy as np
from scipy.optimize import linprog
from CGFCore.GameFile import Game
from CGFCore.ZeroSumGameFile import ZeroSumGame
from CGFCore.NonZeroSumGameFile import NonZeroSumGame
from CGFCore.ComposedGameFile import ComposedGame
from CGFCore.StochasticGameFile import StochasticGame
from CGFCore.BayesianGameFile import BayesianGame
from CGFCore.SequentialGameFile import SequentialGame
from CGFCore.ImperfectInformationGame import ImperfectInformationGame


def test_get_payoff():
    game = Game(np.array([[1, -1], [-1, 1]]))
    assert game.get_payoff([0, 0]) == 1
    assert game.get_payoff([1, 1]) == 1
    assert game.get_payoff([0, 1]) == -1
    assert game.get_payoff([1, 0]) == -1


def test_compute_nash_equilibrium():
    game = ZeroSumGame(np.array([[1, -1], [-1, 1]]))
    value, strategy = game.compute_nash_equilibrium()
    assert np.abs(value - 1) <= 1e-5  # The game value should be 1 for this game.
    assert np.all(
        np.abs(strategy - np.array([1.0, 0.0])) <= 1e-5
    )  # The strategy should be (1.0, 0.0).


def test_compute_nash_equilibrium_non_zero_sum():
    # Create a simple coordination game: (1,1) if both players choose the same action, and (0,0) otherwise.
    game = NonZeroSumGame(np.array([[[1, 0], [0, 1]], [[1, 0], [0, 1]]]))

    # The game has two pure strategy Nash equilibria: (0, 0) and (1, 1).
    initial_strategies = np.array([0, 1])  # Initialize with a non-equilibrium strategy.
    equilibrium_strategies = game.compute_nash_equilibrium(initial_strategies)

    # Check that the result is one of the equilibria.
    assert np.all(equilibrium_strategies == np.array([0, 0])) or np.all(
        equilibrium_strategies == np.array([1, 1])
    ), "The method did not find a Nash equilibrium."


# Helper function to create an instance of ComposedGame
def create_composed_game(composition_type, influence=False):
    game1 = Game(np.array([[1, -1], [-1, 1]]))
    game2 = Game(np.array([[2, -2], [-2, 2]]))
    return ComposedGame(game1, game2, composition_type, influence)


# Test for sequential composition
def test_composed_game_sequential():
    composed_game = create_composed_game("sequential")
    assert composed_game.get_payoff([0, 0, 0, 0]) == 3
    assert composed_game.get_payoff([1, 1, 1, 1]) == 3
    assert composed_game.get_payoff([0, 1, 1, 0]) == -3
    assert composed_game.get_payoff([1, 0, 0, 1]) == -3


# Test for parallel composition
def test_composed_game_parallel():
    composed_game = create_composed_game("parallel")
    assert composed_game.get_payoff([0, 0, 0, 0]) == 2
    assert composed_game.get_payoff([1, 1, 1, 1]) == 2
    assert composed_game.get_payoff([0, 1, 1, 0]) == -1
    assert composed_game.get_payoff([1, 0, 0, 1]) == -1


# Running the tests
test_composed_game_sequential()
test_composed_game_parallel()
"Tests passed!"


# Example usage of the new classes
seq_game = SequentialGame([[[3, 2], [1, 4]], [[2, 3], [4, 1]]])
subgame_perfect_eq = seq_game.compute_subgame_perfect_equilibrium()
print("Subgame Perfect Equilibrium:", subgame_perfect_eq)

bayesian_game = BayesianGame(
    [[[1, 0], [0, 1]], [[1, 0], [0, 1]]], [[0.6, 0.4], [0.4, 0.6]]
)
bayesian_nash_eq = bayesian_game.compute_bayesian_nash_equilibrium()
print("Bayesian Nash Equilibrium:", bayesian_nash_eq)


def test_compute_nash_equilibrium():
    game = ZeroSumGame(np.array([[1, -1], [-1, 1]]))
    value, strategy = game.compute_nash_equilibrium()
    print("Value: ", value)
    print("Strategy: ", strategy)
    assert np.abs(value - 1) <= 1e-5  # The game value should be 1 for this game.
    assert np.all(
        np.abs(strategy - np.array([1.0, 0.0])) <= 1e-5
    )  # The strategy should be (1.0, 0.0).


def test_compute_nash_equilibrium_non_zero_sum():
    # Create a simple coordination game: (1,1) if both players choose the same action, and (0,0) otherwise.
    game = NonZeroSumGame(np.array([[[1, 0], [0, 1]], [[1, 0], [0, 1]]]))

    # The game has two pure strategy Nash equilibria: (0, 0) and (1, 1).
    initial_strategies = np.array([0, 1])  # Initialize with a non-equilibrium strategy.
    equilibrium_strategies = game.compute_nash_equilibrium(initial_strategies)
    print("Equilibrium strategies: ", equilibrium_strategies)

    # Check that the result is one of the equilibria.
    assert np.all(equilibrium_strategies == np.array([0, 0])) or np.all(
        equilibrium_strategies == np.array([1, 1])
    ), "The method did not find a Nash equilibrium."


test_compute_nash_equilibrium_non_zero_sum()
test_get_payoff()
test_compute_nash_equilibrium()


def test_compute_markov_perfect_equilibrium():
    transition_matrix = [[[0.7, 0.1], [0.5, 0.5]], [[0.5, 0.5], [0.1, 0.7]]]

    payoff_matrix = [[[2, -1], [-1, 2]], [[-1, 2], [2, -1]]]

    # Create a game
    game = StochasticGame(transition_matrix, payoff_matrix)

    # Compute the Markov perfect equilibrium
    value, best_response = game.compute_markov_perfect_equilibrium()

    print("Value: ", value)
    print("Best response: ", best_response)

    assert value is not None
    assert best_response is not None


def test_compute_markov_perfect_equilibrium_imperfect_information():
    transition_matrix = [[[0.7, 0.1], [0.5, 0.5]], [[0.5, 0.5], [0.1, 0.7]]]

    payoff_matrix = [[[1, 0], [0, 1]], [[0, 1], [1, 0]]]

    signal_matrix = [[0.9, 0.1], [0.2, 0.8]]

    # Create a game with imperfect information
    game = ImperfectInformationGame(transition_matrix, payoff_matrix, signal_matrix)

    # Compute the Markov perfect equilibrium
    value, best_response = game.compute_markov_perfect_equilibrium()

    print("Value: ", value)
    print("Best response: ", best_response)

    assert value is not None
    assert best_response is not None


test_compute_markov_perfect_equilibrium_imperfect_information()
