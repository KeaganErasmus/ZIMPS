from .action_strategy import ActionStrategy


class ShelveLoadStrategy(ActionStrategy):
    def execute(self, game, filename):
        game.shelve_load(filename)
