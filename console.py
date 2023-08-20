import cmd
from game import Game


class Console(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        with open("commands.txt", 'r') as file:
            print(f'Commands: ')
            for lines in file:
                print(f"{lines}")
            print("\n")

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
            print(str(TypeError))
            print(err)

    def do_cower(self):
        """
        Choose to curl up into a corner and hide.
        """
        try:
            self.game.cower()
        except TypeError as err:
            print(str(TypeError))
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
        """
        Loads the serialized objects in the pickle files
        """
        self.game.load_game(args)

    def do_details(self, args):
        """
        Prints the players details: Location, Health, Attack and Items
        """
        self.game.get_details()
