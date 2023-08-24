import cmd
from game import Game


class Console(cmd.Cmd):
    """
    Keagan Created class
    """
    def __init__(self):
        cmd.Cmd.__init__(self)

        """
        Keagan
        """
        with open("commands.txt", 'r') as file:
            print('Commands: ')
            for lines in file:
                print(f"{lines}")
            print("\n")

        self.prompt = ">>> "
        self.game = Game()

    def do_go(self, direction):
        """
        Choose a direction to go from the current room.
        Syntax: go [direction] where direction is either \'N\' (for
        north), \'E\' (for east), \'S\' (for south), \'W\' (for west).

        Keagan try check
        Sam if check
        Christian turn functionality
        """
        if not self.game.check_game_state():
            try:
                self.game.player_turn(direction)
            except TypeError as err:
                print(str(err))

    def do_bash(self, direction):
        """
        Choose to bash through a wall.

        Christian
        """
        self.game.bash_through_wall(direction)

    def do_totem(self, arg):
        """
        Choose to find or burry the totem.

        Christian
        """
        try:
            self.game.find_or_burry_totem()
        except TypeError as err:
            print(str(err))

    def do_cower(self, arg):
        """
        Choose to curl up into a corner and hide.

        Christian
        """
        try:
            self.game.cower()
        except TypeError as err:
            print(str(err))

    def do_quit(self, arg):
        """
        Quits the current game.

        Christian
        """
        print("Goodbye")
        self.game.gui.root.destroy()
        return True

    def do_save(self, filename):
        """
        Allows the player to save the current game state to a file.

        save file will be created when the user quits the game

        Sam
        """
        self.game.save_game()

    def do_load(self, args):
        """
        Loads the serialized objects in the pickle files

        Sam
        """
        self.game.load_game(args)

    def do_details(self, args):
        """
        Prints the players details: Location, Health, Attack and Items

        Keagan
        """
        self.game.get_details()

    def do_coords(self, args):
        """
        Shows the coordinates of a compass

        Keagan
        """
        print("  N\nW\tE\n  S")
