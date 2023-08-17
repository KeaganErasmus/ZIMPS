from PIL import Image
import random
import json

IMAGE_PATH = 'assets/tiles.jpg'
JSON_PATH = 'assets/tiles.json'


class Tile:
    """
    A tile is a single square on the game board.
    """

    def __init__(self, image, name, exits):
        self.image = image
        self.name = name
        self.exits = exits

    def display(self):
        # self.image.show()
        max_name_len = 15  # Set this to the length of the longest name
        padded_name = self.name.center(max_name_len)  # Center the name

        top_exit = ' ' if self.exits['N'] else '_'
        right_exit = ' ' if self.exits['E'] else '|'
        bottom_exit = ' ' if self.exits['S'] else '_'
        left_exit = ' ' if self.exits['W'] else '|'

        print(f" {top_exit * (max_name_len + 2)} ")
        print(f"+{' ' * (max_name_len + 2)}+")
        print(f"{left_exit} {padded_name} {right_exit}")
        print(f"+{bottom_exit * (max_name_len + 2)}+")
        print('')

    def possible_exits(self):
        return [direction for direction, is_exit in self.exits.items() if is_exit]

    def rotate_tile(self, chosen_entry, chosen_exit):
        """
        Rotate new tile to align the chosen entry with the chosen exit from the previous tile.
        """
        rotations_needed = {'N': {'N': 2, 'E': 1, 'S': 0, 'W': 3},
                            'E': {'N': 3, 'E': 2, 'S': 1, 'W': 0},
                            'S': {'N': 0, 'E': 3, 'S': 2, 'W': 1},
                            'W': {'N': 1, 'E': 0, 'S': 3, 'W': 2}}[chosen_exit][chosen_entry]

        for _ in range(rotations_needed):
            self.exits = {direction: self.exits[prev_dir]
                          for direction, prev_dir in zip('NESW', 'WNES')}
            self.image = self.image.rotate(-90)

        return self


class TileDeck:
    """
    A tile deck is a collection of tiles that can be drawn from.
    """

    def __init__(self, deck_type, image_path=IMAGE_PATH, json_path=JSON_PATH):
        self.tiles = []
        self.image_path = image_path

        tile_metadata = self.load_metadata(deck_type, json_path)
        self.initialize_tiles(tile_metadata)

    def load_metadata(self, deck_type, json_path):
        try:
            with open(json_path, 'r') as file:
                metadata_dict = json.load(file)
            tile_metadata = metadata_dict['OUTDOOR_TILES'] if deck_type == 'outdoor' else metadata_dict['INDOOR_TILES']
            return tile_metadata
        except FileNotFoundError:
            print(
                f"File {json_path} not found. Please ensure the path is correct.")
            return None
        except json.JSONDecodeError:
            print(
                f"Error decoding JSON from {json_path}. Please ensure the file is formatted correctly.")
            return None

    def initialize_tiles(self, tile_metadata):
        if tile_metadata is None:
            return

        image = Image.open(self.image_path)
        rows, cols = 4, 4
        tile_width = image.width // cols
        tile_height = image.height // rows
        index = 1
        start_row = 0 if 'Garden' in [tile['name']
                                      for tile in tile_metadata.values()] else 2

        for i in range(start_row, start_row + rows // 2):
            for j in range(cols):
                left = j * tile_width
                top = i * tile_height
                right = (j + 1) * tile_width
                bottom = (i + 1) * tile_height
                tile_image = image.crop((left, top, right, bottom))
                metadata = tile_metadata[str(index)]
                tile = Tile(tile_image, metadata['name'], metadata['exits'])
                self.tiles.append(tile)
                index += 1

        random.shuffle(self.tiles)
        self.number_of_tiles = len(self.tiles)

    def draw_tile_by_name(self, name):
        for i, tile in enumerate(self.tiles):
            if tile.name == name:
                return self.tiles.pop(i)

    def draw(self):
        if self.tiles:
            tile = self.tiles.pop(0)
            self.number_of_tiles -= 1
            return tile


class IndoorTileDeck(TileDeck):
    def __init__(self):
        super().__init__('indoor')


class OutdoorTileDeck(TileDeck):
    def __init__(self):
        super().__init__('outdoor')
