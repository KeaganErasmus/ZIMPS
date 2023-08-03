from GUI.gui import GUI
from console import console


def main():
    # app = GUI()
    print("Welcome to Zombies in my pocket")
    view = console("help", "start", "stop", "quit")

    while view.user_input() != "quit":
        view.run_commands()


if __name__ == "__main__":
    main()
