from .action_strategy import ActionStrategy


class JsonSaveStrategy(ActionStrategy):
    def execute(self, game, filename):
        game.json_save(filename)
