from cards import CardDeck
from tiles import OutdoorTileDeck, IndoorTileDeck
from GUI.gui import GUI
from player import Player


class Board:
    """
    Class for setting up the board, and tiles
    """

    def __init__(self):
        self.gui = GUI()
        self.dev_cards = CardDeck()
        self.outdoor_tiles = OutdoorTileDeck()
        self.indoor_tiles = IndoorTileDeck()
        self.time = '9 PM'
        self.board = {}
        self.patio_tile = None
        self.initialize_game()
        # Start the GUI main loop
        self.gui.root.mainloop()

    def initialize_game(self):
        # Place the 'Foyer' tile on the board
        foyer_tile = self.indoor_tiles.draw_tile_by_name('Foyer')
        self.gui.place_tile(foyer_tile, 5, 3)
        self.board[(5, 3)] = foyer_tile

        # Set aside the 'Patio' tile
        self.patio_tile = self.outdoor_tiles.draw_tile_by_name('Patio')