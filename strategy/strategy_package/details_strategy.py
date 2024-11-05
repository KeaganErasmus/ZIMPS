from .action_strategy import ActionStrategy


class DetailsStrategy(ActionStrategy):
    def execute(self, game):
        game.get_details()
