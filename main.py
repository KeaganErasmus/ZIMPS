from GUI.gui import GUI
from console import Console
from pickling import Pickling
from cmdconsole import CMDConsole


def main():
    # app = GUI()
    print("Welcome to Zombies in my pocket")
    console = Console()

    console.cmdloop()


if __name__ == "__main__":
    main()
