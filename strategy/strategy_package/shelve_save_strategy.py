from .action_strategy import ActionStrategy


class ShelveSaveStrategy(ActionStrategy):
    def execute(self, game, filename):
        if not filename:
            print("Please re-enter command with filename to save to")
        else:
            game.shelve_save(filename)
