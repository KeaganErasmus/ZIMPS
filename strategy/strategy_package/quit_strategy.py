from .action_strategy import ActionStrategy
import sys


class QuitStrategy(ActionStrategy):
    def execute(self, game):
        print("Goodbye")
        game.gui.root.destroy()
        sys.exit(0)
        return True
