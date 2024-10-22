import cmd
from game import Game
import sys


# Strategy Base Class
class ActionStrategy:
    def execute(self, game, *args):
        raise NotImplementedError("This method should be overridden by subclasses")

# Concrete Strategies for each action
class GoStrategy(ActionStrategy):
    def execute(self, game, direction):
        if not game.check_game_state():
            try:
                game.player_turn(direction)
            except TypeError as err:
                print(str(err))

class BashStrategy(ActionStrategy):
    def execute(self, game, direction):
        game.bash_through_wall(direction)

class TotemStrategy(ActionStrategy):
    def execute(self, game):
        try:
            game.find_or_burry_totem()
        except TypeError as err:
            print(str(err))

class CowerStrategy(ActionStrategy):
    def execute(self, game):
        try:
            game.cower()
        except TypeError as err:
            print(str(err))

class SaveStrategy(ActionStrategy):
    def execute(self, game, filename=None):
        game.save_game()

class ShelveSaveStrategy(ActionStrategy):
    def execute(self, game, filename):
        if not filename:
            print("Please re-enter command with filename to save to")
        else:
            game.shelve_save(filename)

class ShelveLoadStrategy(ActionStrategy):
    def execute(self, game, filename):
        game.shelve_load(filename)

class JsonSaveStrategy(ActionStrategy):
    def execute(self, game, filename):
        game.json_save(filename)

class JsonLoadStrategy(ActionStrategy):
    def execute(self, game, filename):
        game.json_load(filename)

class LoadStrategy(ActionStrategy):
    def execute(self, game, args):
        game.load_game(args)

class QuitStrategy(ActionStrategy):
    def execute(self, game):
        print("Goodbye")
        game.gui.root.destroy()
        sys.exit(0)
        return True

class DetailsStrategy(ActionStrategy):
    def execute(self, game):
        game.get_details()

class CoordsStrategy(ActionStrategy):
    def execute(self, game):
        print("  N\nW\tE\n  S")

# Console class to manage command-line input
class Console(cmd.Cmd):
    """
    Command-line interface for the game.
    """
    def __init__(self, start_coordinates, board_size, card_data, card_image):
        cmd.Cmd.__init__(self)
        self.prompt = ">>> "
        self.game = Game(start_coordinates, board_size, card_data, card_image)
        self.strategies = {
            "go": GoStrategy(),
            "bash": BashStrategy(),
            "totem": TotemStrategy(),
            "cower": CowerStrategy(),
            "quit": QuitStrategy(),
            "save": SaveStrategy(),
            "shelve_save": ShelveSaveStrategy(),
            "shelve_load": ShelveLoadStrategy(),
            "json_save": JsonSaveStrategy(),
            "json_load": JsonLoadStrategy(),
            "load": LoadStrategy(),
            "details": DetailsStrategy(),
            "coords": CoordsStrategy(),
        }

        with open("commands.txt", 'r') as file:
            print('Commands: ')
            for lines in file:
                print(f"{lines}")
            print("\n")

    def do_action(self, action, *args):
        """
        Executes the corresponding action by using the associated strategy.
        """
        strategy = self.strategies.get(action)
        if strategy:
            strategy.execute(self.game, *args)
        else:
            print(f"Unknown action: {action}")

    # Wrappers for the actual commands
    def do_go(self, direction):
        self.do_action("go", direction)

    def do_bash(self, direction):
        self.do_action("bash", direction)

    def do_totem(self, arg):
        self.do_action("totem")

    def do_cower(self, arg):
        self.do_action("cower")

    def do_quit(self, arg):
        return self.do_action("quit")

    def do_save(self, filename):
        self.do_action("save", filename)

    def do_shelve_save(self, filename):
        """
        Saves with shelve.
        Syntax: shelve_save [filename]
        """
        self.do_action("shelve_save", filename)

    def do_shelve_load(self, filename):
        """
        Loads with shelve.
        Syntax: shelve_load [filename]
        """
        self.do_action("shelve_load", filename)

    def do_json_save(self, filename):
        self.do_action("json_save", filename)

    def do_json_load(self, filename):
        self.do_action("json_load", filename)

    def do_load(self, args):
        self.do_action("load", args)

    def do_details(self, args):
        self.do_action("details")

    def do_coords(self, args):
        self.do_action("coords")
