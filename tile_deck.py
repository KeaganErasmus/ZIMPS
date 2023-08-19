import json
import random
from PIL import Image
from tile import Tile

IMAGE_PATH = 'assets/tiles.jpg'
DATA_PATH = 'assets/tiles.json'


class TileDeck:
    """
    A tile deck is a collection of tiles that can be drawn from.
    """

    def __init__(self, deck_type, image_path=IMAGE_PATH, json_path=DATA_PATH):
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
