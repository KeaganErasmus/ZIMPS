import cmd
from game import Game


class Console(cmd.Cmd):
    """
    Keagan Created class
    """

    def __init__(self, start_coordinates, board_size, card_data, card_image):
        cmd.Cmd.__init__(self)

        """
        Keagan
        """
        self.prompt = ">>> "
        self.game = Game(start_coordinates, board_size, card_data, card_image)
        with open("commands.txt", 'r') as file:
            print('Commands: ')
            for lines in file:
                print(f"{lines}")
            print("\n")

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

    def do_shelve_save(self, filename):
        """
        allows the player to save the game data to a shelve file
        """
        try:
            self.game.shelve_save(filename)
        except:
            print("Please enter a filename to save to")

        # if not filename:
        #     print("Please enter a filename to save to")
        # else:
        #     self.game.shelve_save(filename)

    def do_shelve_load(self, filename):
        """
        allows the player to load a shelve file
        """
        self.game.shelve_load(filename)

    def do_json_save(self, filename):
        """
        Save the current player state to a json file
        """
        self.game.json_save(filename)

    def do_json_load(self, filename):
        """
        load up a json file
        """
        self.game.json_load(filename)

    def do_load(self, args):
        """
        Load by itself will load all current pickled player data
        if you specify a filepath when loading you will load the shelve file
        the default filename is player_data (load player_data)

        sam
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
