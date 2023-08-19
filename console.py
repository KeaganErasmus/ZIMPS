import cmd
from game import Game


class Console(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        print("Commands: help, go, quit")
        self.prompt = ">>> "
        self.game = Game()

    def do_go(self, direction):
        """
        Choose a direction to go from the current room.
        Syntax: go [direction] where direction is either \'n\' (for north), \'e\' (for east), \'s\' (for south), \'w\' (for west).
        """
        try:
            self.game.player_turn(direction)
        except TypeError as err:
            print("Please enter a direction")

    def do_quit(self, arg):
        """
        Quits the current game.
        """
        print("Goodbye")
        return True
