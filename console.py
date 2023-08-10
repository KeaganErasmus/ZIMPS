class Console:
    """
    Console that displays text and allows for user input
    """

    def __init__(self, *args) -> None:
        self.args = args
        self.userinput = ""

    def print_commands(self):
        """
        Print the commands that can be used 
        """
        print(f'These are the commands that you can use: \n{self.args}')

    def user_input(self):
        """
        Takes the raw input from a user and displays the message
        """
        self.userinput = input("To see all commands type help: ").strip().lower()

    def run_commands(self):
        if self.userinput == "help":
            self.print_commands()
        else:
            print("That is not a recognized command: Type help to see all commands")
