
class OpenGame:
    def __init__(self, players):
        self.players = players
        self.strategies = {player: None for player in players}
        self.history = []
        self.future = []

    def set_strategy(self, player, strategy):
        self.strategies[player] = strategy

    def play(self, history):
        raise NotImplementedError("Each game must implement its own play function.")

    def coplay(self, future, outcome):
        raise NotImplementedError("Each game must implement its own coplay function.")

    def utility(self, history, future, outcome, player):
        raise NotImplementedError("Each game must implement its own utility function.")

class PrisonersDilemma(OpenGame):
    def __init__(self, players):
        super().__init__(players)
        self.payoffs = {
            ("cooperate", "cooperate"): {player: 2 for player in players},
            ("cooperate", "defect"): {player: 0 if player == "player1" else 3 for player in players},
            ("defect", "cooperate"): {player: 3 if player == "player1" else 0 for player in players},
            ("defect", "defect"): {player: 1 for player in players}
        }

    def play(self, history):
        return tuple(self.strategies[player] for player in self.players)

    def coplay(self, future, outcome):
        return future

    def utility(self, history, future, outcome, player):
        return self.payoffs[outcome][player]

def test_open_games():
    # Test PrisonersDilemma
    game = PrisonersDilemma(["player1", "player2"])

    game.set_strategy("player1", "cooperate")
    game.set_strategy("player2", "defect")

    history = ["previous_play"]
    outcome = game.play(history)
    future = game.coplay(["potential_future"], outcome)
    utilities = {player: game.utility(history, future, outcome, player) for player in game.players}

    print(f"Outcome: {outcome}")
    print(f"Utilities: {utilities}")

test_open_games()

class CompositeOpenGame(OpenGame):
    def __init__(self, game1, game2, composition_type="sequential"):
        super().__init__(game1.players + game2.players)
        self.game1 = game1
        self.game2 = game2
        self.composition_type = composition_type

    def play(self, history):
        if self.composition_type == "sequential":
            outcome1 = self.game1.play(history)
            outcome2 = self.game2.play(history + [outcome1])
            return outcome1, outcome2
        elif self.composition_type == "parallel":
            outcome1 = self.game1.play(history)
            outcome2 = self.game2.play(history)
            return outcome1, outcome2
        else:
            raise ValueError("Invalid composition type")

    def coplay(self, future, outcome):
        future1, future2 = future
        outcome1, outcome2 = outcome
        coplayed_future1 = self.game1.coplay(future1, outcome1)
        coplayed_future2 = self.game2.coplay(future2, outcome2)
        return coplayed_future1, coplayed_future2

    def utility(self, history, future, outcome, player):
        outcome1, outcome2 = outcome
        if player in self.game1.players:
            coplayed_future1, _ = self.coplay(future, outcome)
            return self.game1.utility(history, coplayed_future1, outcome1, player)
        elif player in self.game2.players:
            _, coplayed_future2 = self.coplay(future, outcome)
            return self.game2.utility(history, coplayed_future2, outcome2, player)
        else:
            raise ValueError(f"{player} is not a player in this composite game")

def test_composite_open_games():
    game1 = PrisonersDilemma(["player1", "player2"])
    game2 = PrisonersDilemma(["player3", "player4"])

    game1.set_strategy("player1", "cooperate")
    game1.set_strategy("player2", "defect")
    game2.set_strategy("player3", "defect")
    game2.set_strategy("player4", "cooperate")

    composite_game = CompositeOpenGame(game1, game2, "parallel")

    history = ["previous_play"]
    outcome = composite_game.play(history)
    future = composite_game.coplay(["potential_future1", "potential_future2"], outcome)
    utilities = {player: composite_game.utility(history, future, outcome, player) for player in composite_game.players}

    print(f"Outcome: {outcome}")
    print(f"Utilities: {utilities}")

test_composite_open_games()