class console:
    """
    Console that displays text and allows for user input
    """

    def __init__(self, args: list[str]) -> None:
        self.args = args

    def print_commands(self):
        """
        Print the commands that can be used 
        """
        print(f'These are the commands that you can use: \n{self.args}')

    def user_input(self) -> str:
        """
        Takes the raw input from a user and displays the message
        """
        user_input: str = input("To see all commands type help: ").strip().lower()

        return user_input

    def run_commands(self):
        if self.user_input() == "help":
            self.print_commands()
        else:
            print("That is not a recognized command: Type help to see all commands")
