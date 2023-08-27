import argparse
from console import Console


def main():
    parser = argparse.ArgumentParser(description='Zombies in my Pocket game.')
    parser.add_argument('--x', type=int, default=5,
                        help='The start x-coordinate for the player.')
    parser.add_argument('--y', type=int, default=3,
                        help='The start y-coordinate for the player.')
    args = parser.parse_args()

    print("Welcome to Zombies in my pocket")
    start_coordinates = (args.x, args.y)
    run = Console(start_coordinates)
    run.cmdloop()
    run.game.gui.root.mainloop()


if __name__ == "__main__":
    main()
