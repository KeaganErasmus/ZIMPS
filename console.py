import cmd
from game import Game


class Console(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        print("Commands: help, go [direction], cower, quit, save")
        self.prompt = ">>> "
        self.game = Game()

    def do_go(self, direction):
        """
        Choose a direction to go from the current room. Syntax: go [direction] where direction is either \'N\' (for
        north), \'E\' (for east), \'S\' (for south), \'W\' (for west).
        """
        try:
            self.game.player_turn(direction)
        except TypeError as err:
            print(TypeError.__str__())
            print(err)

    def do_cower(self):
        """
        Choose to curl up into a corner and hide.
        """
        try:
            self.game.cower()
        except TypeError as err:
            print(TypeError.__str__())
            print(err)

    def do_quit(self, arg):
        """
        Quits the current game.
        """
        print("Goodbye")
        self.game.gui.root.destroy()
        return True

    def do_save(self, filename):
        """
        Allows the player to save the current game state to a file.

        save file will be created when the user quits the game
        """
        self.game.save_game(filename)

    def do_load(self, args):
        self.game.load_game(args)
