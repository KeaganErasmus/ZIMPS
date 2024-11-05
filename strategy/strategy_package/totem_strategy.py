from .action_strategy import ActionStrategy


class TotemStrategy(ActionStrategy):
    def execute(self, game):
        try:
            game.find_or_burry_totem()
        except TypeError as err:
            print(str(err))
