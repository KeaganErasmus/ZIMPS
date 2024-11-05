from action_strategy import ActionStrategy


class CoordsStrategy(ActionStrategy):
    def execute(self, game):
        print("  N\nW\tE\n  S")
