from GUI.gui import GUI
from card_deck import CardDeck
from tile_deck import OutdoorTileDeck, IndoorTileDeck


class Board:
    """
    Class for setting up the game commponents and GUI.
    """

    def __init__(self, start_time='9 PM', start_coordinates=(5, 3)):
        self.time = start_time
        self.tile_map = {}
        self.patio_tile = None
        self.gui = GUI()
        self.dev_cards = CardDeck()
        self.outdoor_tiles = OutdoorTileDeck()
        self.indoor_tiles = IndoorTileDeck()
        self._setup(start_coordinates)

    def _setup(self, start_coordinates):
        """Intialize the game board.

        Args:
            start_coordinates (tuple): The x, y starting coordinates.
        """
        # Place the 'Foyer' tile at the start coordinates
        foyer_tile = self.indoor_tiles.draw_tile_by_name('Foyer')
        self.tile_map[start_coordinates] = foyer_tile
        self.gui.place_tile(foyer_tile, *start_coordinates)

        # Set aside the 'Patio' tile
        self.patio_tile = self.outdoor_tiles.draw_tile_by_name('Patio')

    def update_time(self):
        """
        Update the time and create a new dev card deck.
        """
        self.time = '10 PM' if self.time == '9 PM' else '11 PM'
        self.dev_cards = CardDeck()

    def is_explored(self, location):
        return location in self.tile_map
