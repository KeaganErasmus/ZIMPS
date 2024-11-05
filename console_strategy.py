import cmd
from game import Game
import sys
from strategy_package import *


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
