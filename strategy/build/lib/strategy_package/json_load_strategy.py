from action_strategy import ActionStrategy


class JsonLoadStrategy(ActionStrategy):
    def execute(self, game, filename):
        game.json_load(filename)
