import argparse
from abc import ABC, abstractmethod


class GameConfigFactory(ABC):
    @abstractmethod
    def create_game_config(self):
        pass


class CustomGameConfigFactory(GameConfigFactory):
    def create_game_config(self):
        return CustomGameConfig()


class CustomGameConfig:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Zombies in my Pocket game')
        self.setup_arguments()

    def setup_arguments(self):
        self.parser.add_argument('--x', type=int, default=5,
                                 help='The start x-coordinate for the player.')
        self.parser.add_argument('--y', type=int, default=3,
                                 help='The start y-coordinate for the player.')
        self.parser.add_argument('--rows', type=int, default=7,
                                 help="The number of rows on the Board")
        self.parser.add_argument('--cols', type=int, default=7,
                                 help="The number of cols on the Board")
        self.parser.add_argument('--cards_data', type=str,
                                 default='assets/dev_cards.json',
                                 help='The path to the tiles data JSON file.')
        self.parser.add_argument('--cards_image', type=str,
                                 default='assets/dev_cards.jpg',
                                 help='The path to the tiles image file.')

    def parse_arguments(self):
        args = self.parser.parse_args()
        # Validate the coordinates against the board size
        if args.x >= args.cols or args.y >= args.rows:
            print(f"Invalid arguments: Coordinates ({args.x}, {args.y}) "
                  f"Out of board bounds: ({args.rows}, {args.cols})")
            return None
        return args
