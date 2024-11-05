from .action_strategy import ActionStrategy


class SaveStrategy(ActionStrategy):
    def execute(self, game, filename=None):
        game.save_game()
