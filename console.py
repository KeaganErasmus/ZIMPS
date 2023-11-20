import cmd
from game import Game
from consoleStrategy import *


class Console(cmd.Cmd):
    def __init__(self, start_coordinates, board_size, card_data, card_image):
        cmd.Cmd.__init__(self)
        self.prompt = ">>> "
        self.game = Game(start_coordinates, board_size, card_data, card_image)
        self.strategy = None  # Will hold the current strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_action(self, action, args):
        if not self.game.check_game_state() and self.strategy:
            self.strategy.execute(self.game, args)

    def do_go(self, args):
        self.set_strategy(GoStrategy())
        self.do_action("go", args)

    def do_bash(self, args):
        self.set_strategy(BashStrategy())
        self.do_action("bash", args)

    def do_totem(self, args):
        self.set_strategy(TotemStrategy())
        self.do_action("totem", args)

    def do_cower(self, args):
        self.set_strategy(CowerStrategy())
        self.do_action("cower", args)

    def do_quit(self, args):
        self.set_strategy(QuitStrategy())
        self.do_action("quit", args)
        return True

    def do_save(self, args):
        self.set_strategy(SaveStrategy())
        self.do_action("save", args)

    def do_shelve_save(self, args):
        self.set_strategy(ShelveSaveStrategy())
        self.do_action("shelve_save", args)

    def do_shelve_load(self, args):
        self.set_strategy(ShelveLoadStrategy())
        self.do_action("shelve_load", args)

    def do_json_save(self, args):
        self.set_strategy(JsonSaveStrategy())
        self.do_action("json_save", args)

    def do_json_load(self, args):
        self.set_strategy(JsonLoadStrategy())
        self.do_action("json_load", args)

    def do_load(self, args):
        self.set_strategy(LoadStrategy())
        self.do_action("load", args)

    def do_details(self, args):
        self.set_strategy(DetailsStrategy())
        self.do_action("details", args)

    def do_coords(self, args):
        self.set_strategy(CoordsStrategy())
        self.do_action("coords", args)

