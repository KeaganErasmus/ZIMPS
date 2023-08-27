import argparse
from console import Console


def main():
    parser = argparse.ArgumentParser(description='Zombies in my Pocket game.')
    parser.add_argument('--x', type=int, default=5,
                        help='The start x-coordinate for the player.')
    parser.add_argument('--y', type=int, default=3,
                        help='The start y-coordinate for the player.')
    
    parser.add_argument('--rows', type=int, default=7,
                        help="The number of rows on the Board")
    parser.add_argument('--cols', type=int, default=7,
                    help="The number of cols on the Board")   
    args = parser.parse_args()

    print("Welcome to Zombies in my pocket")
    start_coordinates = (args.x, args.y)
    board_size = (args.rows, args.cols)
    
    run = Console(start_coordinates, board_size)
    run.cmdloop()
    run.game.gui.root.mainloop()


if __name__ == "__main__":
    main()
