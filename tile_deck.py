# --------------------------------------------------------------
# tile_deck.py
# --------------------------------------------------------------
# Author: Christian Diekmann
#
# Description:
# A deck of tiles represented as a Python class.
# Provides methods for initializing the deck from JSON and image files,
# shuffling, discarding, and drawing tiles.
# ---------------------------------------------------------------
import json
import random
from PIL import Image, UnidentifiedImageError
from tile import Tile


class TileDeckInitializationError(Exception):
    pass


class TileDeck:
    """
    A tile deck is a collection of tiles that can be drawn from.
    """

    def __init__(self, deck_type, image_path='assets/tiles.jpg',
                 json_path='assets/tiles.json'):
        self.tiles = []
        self.image_path = image_path

        tile_metadata = self._load_metadata(deck_type, json_path)
        self._initialize_tiles(deck_type, tile_metadata)

    def _load_metadata(self, deck_type, json_path):
        try:
            with open(json_path, 'r') as file:
                metadata_dict = json.load(file)
        except FileNotFoundError as e:
            raise TileDeckInitializationError(
                f"File {json_path} not found.") from e
        except json.JSONDecodeError as e:
            raise TileDeckInitializationError(
                f"Error decoding JSON from {json_path}.") from e

        key = 'OUTDOOR' if deck_type == 'outdoor' else 'INDOOR'
        tile_metadata = metadata_dict.get(key)

        if tile_metadata is None:
            raise TileDeckInitializationError(
                f"Metadata for deck type '{deck_type}' "
                "not found in {json_path}.")

        return tile_metadata

    def _initialize_tiles(self, decktype, tile_metadata, rows=4, cols=4):
        try:
            image = Image.open(self.image_path)
        except FileNotFoundError as e:
            raise TileDeckInitializationError(
                f"Tile image file {self.image_path} not found.") from e
        except UnidentifiedImageError as e:
            raise TileDeckInitializationError(
                f"Invalid tile image for file {self.image_path}.") from e

        tile_width = image.width // cols
        tile_height = image.height // rows
        index = 1
        start_row = 0 if decktype == 'outdoor' else 2

        for i in range(start_row, start_row + rows // 2):
            for j in range(cols):
                left = j * tile_width
                top = i * tile_height
                right = (j + 1) * tile_width
                bottom = (i + 1) * tile_height
                tile_image = image.crop((left, top, right, bottom))
                metadata = tile_metadata[str(index)]
                tile = Tile(
                    tile_image, metadata['name'], metadata['exits'], decktype)
                self.tiles.append(tile)
                index += 1

        random.shuffle(self.tiles)
        self.count = len(self.tiles)

    def draw_by_name(self, name):
        """
        Draws a tile from the deck by name.
        """
        for i, tile in enumerate(self.tiles):
            if tile.name == name:
                self.count -= 1
                return self.tiles.pop(i)

    def draw(self):
        """
        Draws a tile from the deck.
        """
        if self.count > 0:
            tile = self.tiles.pop(0)
            self.count -= 1
            return tile
        return None


class IndoorTiles(TileDeck):
    def __init__(self):
        super().__init__('indoor')


class OutdoorTiles(TileDeck):
    def __init__(self):
        super().__init__('outdoor')
