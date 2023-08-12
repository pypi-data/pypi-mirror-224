from CGFCore.GameFile import Game
import numpy as np
from scipy.optimize import linprog


class ZeroSumGame(Game):
    def compute_nash_equilibrium(self):
        num_actions = self.payoff_matrix.shape[0]
        # number of actions a player can take in this game. The number of actions corresponds to the number of rows in the payoff matrix for the game.
        # The payoff matrix is a way of summarizing a game by listing out the payoffs of all possible strategies a player can take.
        c = np.ones(num_actions)
        # creating a coefficient vector for the linear programming problem.
        # Each element in this vector represents the weight (or coefficient) for the corresponding decision variable in the linear programming problem.
        A_ub = np.vstack([self.payoff_matrix.T, -np.eye(num_actions)])
        # constructing the inequality constraint matrix A_ub. The function np.vstack stacks arrays vertically.
        # So, this line is stacking the transpose of the payoff matrix on top of the negative identity matrix of size num_actions
        b_ub = np.concatenate((np.ones(num_actions), np.zeros(num_actions)), axis=None)
        # creating the inequality constraint vector b_ub.
        # This vector is made by concatenating a vector of ones (of size num_actions) and a vector of zeros (also of size num_actions).

        A_eq = np.ones((1, num_actions))
        b_eq = np.ones(1)
        # defining the equality constraint matrix and vector.
        # Since we have only one constraint that the sum of the probabilities of all actions is 1,
        # the equality constraint matrix A_eq is a row vector of ones, and b_eq is a vector of length 1 with a single element 1.

        result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method="highs")
        # the linprog function from the scipy.optimize module to solve the linear programming problem defined by the coefficients vector c
        # the constraint matrices and vectors A_ub, b_ub, A_eq, and b_eq. The 'highs' method is used as the solver for this linear programming problem.

        value = 1 / result.fun
        # computing the value of the game, which is the reciprocal of the optimal value of the objective function from the linear programming problem.
        strategy = result.x * value
        # The Nash equilibrium strategy is given by the optimal solution to the linear programming problem (stored in result.x) scaled by the game value.

        return value, strategy
