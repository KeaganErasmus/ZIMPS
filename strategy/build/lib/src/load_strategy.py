from action_strategy import ActionStrategy


class LoadStrategy(ActionStrategy):
    def execute(self, game, args):
        game.load_game(args)
