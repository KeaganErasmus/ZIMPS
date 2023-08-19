from console import Console


def main():
    print("Welcome to Zombies in my pocket")
    run = Console()
    while True:
        run.cmdloop()
        run.game.board.gui.root.mainloop()


if __name__ == "__main__":
    main()
