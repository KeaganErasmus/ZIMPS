from GUI.gui import GUI
from console import Console


def main():
    # app = GUI()
    print("Welcome to Zombies in my pocket")
    view = Console()

    view.cmdloop()


if __name__ == "__main__":
    main()
