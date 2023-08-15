from GUI.gui import GUI
from console import Console
from pickling import Pickling
from cmdconsole import CMDConsole


def main():
    # app = GUI()
    print("Welcome to Zombies in my pocket")
    vcon = Console("help", "start", "stop", "quit")
    vcmd = CMDConsole()

    vcmd.cmdloop()

    while vcon.userinput != "quit":
        vcon.user_input()
        vcon.run_commands()


if __name__ == "__main__":
    main()
