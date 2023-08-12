class ComposedGame:
    """Represents a game composed of two other games."""

    def __init__(self, game1, game2, composition_type, influence=False):
        self.game1 = game1
        self.game2 = game2
        self.composition_type = composition_type
        self.influence = influence

    def get_payoff(self, actions):
        """Returns the payoff given a list of actions."""
        payoff1 = self.game1.get_payoff(actions[:2])
        if self.influence:
            actions[2:] = [
                a + payoff1 for a in actions[2:]
            ]  # Modify each action individually.
        payoff2 = self.game2.get_payoff(actions[2:])
        if self.composition_type == "sequential":
            return payoff1 + payoff2
        elif self.composition_type == "parallel":
            return max(payoff1, payoff2)
        else:
            raise ValueError("Invalid composition type")
