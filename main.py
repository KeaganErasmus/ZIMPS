from game import Game
from console import Console
from pickling import Pickling
from cmdconsole import CMDConsole


def main():
    print("Welcome to Zombies in my pocket")
    view = Console()
    view.cmdloop()
    # app = Game()
    # app.gui.root.mainloop()


if __name__ == "__main__":
    main()
