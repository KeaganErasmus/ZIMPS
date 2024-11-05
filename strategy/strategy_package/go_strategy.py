from .action_strategy import ActionStrategy


class GoStrategy(ActionStrategy):
    def execute(self, game, direction):
        if not game.check_game_state():
            try:
                game.player_turn(direction)
            except TypeError as err:
                print(str(err))
