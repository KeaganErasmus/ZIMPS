from card_deck import CardDeck
from tile_deck import OutdoorTileDeck, IndoorTileDeck


class Board:
    """
    Holds the different game commponents. eg Cards, Tiles etc.
    """

    def __init__(self, start_coordinates, start_time='9 PM'):
        self.time = start_time
        self.tile_map = {}
        self.dev_cards = CardDeck()
        self.outdoor_tiles = OutdoorTileDeck()
        self.indoor_tiles = IndoorTileDeck()
        self.patio_tile = self.outdoor_tiles.draw_tile_by_name('Patio')
        self.foyer_tile = self.indoor_tiles.draw_tile_by_name('Foyer')
        self.tile_map[start_coordinates] = self.foyer_tile

    def update_time(self):
        """
        Update the time and create a new dev card deck.
        """
        self.time = '10 PM' if self.time == '9 PM' else '11 PM'
        self.dev_cards = CardDeck()

    def is_explored(self, location):
        return location in self.tile_map
