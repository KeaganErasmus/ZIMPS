class console:
    """
    Console that displays text and allows for user input
    """
    def __init__(self, args: []) -> None:
        self.args = args

        while self.user_input() != "quit":
            self.user_input()
    

    def print_commands(self):
        """
        Print the commands that can be used 
        """
        print(self.args)


    def user_input(self):
        """
        Takes the raw input from a user and displays the message
        """
        user_input = input("To see all commands type help: ").strip().lower()

        if user_input == "help":
            self.print_commands()
        if user_input == "quit":
            return "quit"
        
        return user_input
