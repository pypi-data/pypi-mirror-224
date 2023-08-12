from CGFCore import main
from CGFCore.SequentialGameFile import SequentialGame
from CGFCore.BayesianGameFile import BayesianGame


def run_tests():
    print(main.test_compute_nash_equilibrium())
    print(main.test_compute_nash_equilibrium_non_zero_sum())
    print(main.test_compute_nash_equilibrium())
    print(main.test_composed_game_parallel())
    print(main.test_composed_game_sequential())

    seq_game = SequentialGame([[[3, 2], [1, 4]], [[2, 3], [4, 1]]])
    subgame_perfect_eq = seq_game.compute_subgame_perfect_equilibrium()
    print("Subgame Perfect Equilibrium:", subgame_perfect_eq)

    bayesian_game = BayesianGame(
        [[[1, 0], [0, 1]], [[1, 0], [0, 1]]], [[0.6, 0.4], [0.4, 0.6]]
    )
    bayesian_nash_eq = bayesian_game.compute_bayesian_nash_equilibrium()
    print("Bayesian Nash Equilibrium:", bayesian_nash_eq)
