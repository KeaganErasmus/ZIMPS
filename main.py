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

    parser.add_argument('--cards_data', type=str,
                        default='assets/dev_cards.json',
                        help='The path to the tiles data JSON file.')
    parser.add_argument('--cards_image', type=str,
                        default='assets/dev_cards.jpg',
                        help='The path to the tiles image file.')

    args = parser.parse_args()
    # Validate the coordinates against the board size
    if args.x >= args.cols or args.y >= args.rows:
        print(f"Invalid arguments: Coordinates ({args.x}, {args.y}) "
              f"Out of board bounds: ({args.rows}, {args.cols})")
        return

    start_coordinates = (args.x, args.y)
    board_size = (args.rows, args.cols)

    print("Welcome to Zombies in my pocket")
    run = Console(start_coordinates, board_size,
                  args.cards_data, args.cards_image)
    run.cmdloop()
    run.game.gui.root.mainloop()


if __name__ == "__main__":
    main()
