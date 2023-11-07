from GameConfig import CustomGameConfigFactory
from console import Console


def main():
    factory = CustomGameConfigFactory()
    config = factory.create_game_config()
    args = config.parse_arguments()

    if args:
        start_coordinates = (args.x, args.y)
        board_size = (args.rows, args.cols)
        print("Welcome to Zombies in my pocket")
        run = Console(start_coordinates, board_size,
                      args.cards_data, args.cards_image)

        run.cmdloop()
        run.game.gui.root.mainloop()
        pass


if __name__ == "__main__":
    main()
