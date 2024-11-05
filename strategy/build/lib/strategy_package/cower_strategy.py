from action_strategy import ActionStrategy


class CowerStrategy(ActionStrategy):
    def execute(self, game):
        try:
            game.cower()
        except TypeError as err:
            print(str(err))
