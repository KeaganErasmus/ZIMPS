from console import Console


def main():
    print("Welcome to Zombies in my pocket")
    run = Console()
    run.cmdloop()
    run.game.gui.root.mainloop()



if __name__ == "__main__":
    main()
