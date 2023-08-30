# --------------------------------------------------------------
# board.py
# --------------------------------------------------------------
# Author: Christian Diekmann
#
# Description:
# A board for the Zombie in my Pocket game.
# It holds the different game components. eg Development Cards, Tiles etc.
# ---------------------------------------------------------------
from card_deck import CardDeck
from tile_deck import OutdoorTiles, IndoorTiles


class Board:
    """
    Holds the different game commponents. eg Cards, Tiles etc.
    """

    def __init__(self, start_coordinates, card_data, card_image,
                 start_time='9 PM'):
        self.time = start_time
        self.tile_map = {}  # {(x, y): Tile}
        self.dev_cards = CardDeck(card_data, card_image)
        self.outdoor_tiles = OutdoorTiles()
        self.indoor_tiles = IndoorTiles()
        self.patio_tile = self.outdoor_tiles.draw_by_name('Patio')
        self.foyer_tile = self.indoor_tiles.draw_by_name('Foyer')
        self.tile_map[start_coordinates] = self.foyer_tile

    def update_time(self):
        """
        Update the time and create a new dev card deck.
        """
        self.time = '10 PM' if self.time == '9 PM' else '11 PM'
        self.dev_cards = CardDeck()

    def draw_tile(self, current_room):
        """Draw a tile from the tile deck based on the current room.

        Args:
            current_room (Tile): The room the player is in.

        Returns:
            Tile: The drawn tile.
            str: The tile type. Either 'indoor' or 'outdoor'.
        """
        tile_type = current_room.tile_type
        tile = None
        print()
        if tile_type == "outdoor":
            tile = self.outdoor_tiles.draw()
        elif tile_type == "indoor":
            tile = self.indoor_tiles.draw()

        return tile, tile_type

    def is_explored(self, location):
        """Check if the given location has been explored.

        Args:
            location (tuple): The location to check.

        Returns:
            Bool: True if the location has been explored, False otherwise.
        """
        return location in self.tile_map
