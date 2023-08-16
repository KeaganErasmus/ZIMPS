import cmd


class Console(cmd.Cmd):
    """
    Console that displays text and allows for user input
    """

    def __init__(self) -> None:
        cmd.Cmd.__init__(self)
        self.prompt = ">>"
        self.args = ["help, start, go, quit"]

        print(self.args)

    def do_go(self, direction):
        """
        Choose a direction to go from the current room. Syntax: go [direction] where direction is either \'n\' (for
        north), \'e\' (for east), \'s\' (for south), \'w\' (for west).
        """
        try:
            # this is where we will put the turn logic
            pass
        except TypeError as err:
            print("Please enter a direction")

    def do_quit(self, arg):
        """
        Quits the current game.
        """
        print("Goodbye")
        return True
