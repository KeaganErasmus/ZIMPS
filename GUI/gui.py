from PIL import ImageTk
import tkinter as tk

from GUI.cards import CardDeck
from GUI.tiles import TileDeck


class GUI:
    """
    A GUI for drawing cards from a deck.
    """

    def __init__(self):
        self.dev_cards = CardDeck()
        self.outdoor_tiles = TileDeck(deck_type='outdoor')
        self.indoor_tiles = TileDeck(deck_type='indoor')

        self.root = tk.Tk()
        self.root.title("Zombie in my pocket")

        # Create a label to hold the card image and set the placeholder as the initial image
        self.label_image = tk.Label(self.root)
        self.label_image.pack()

        # Create a label to show the number of cards
        self.label_number_of_cards = tk.Label(
            self.root, text=f"Development Cards: {self.dev_cards.get_number_of_cards()}")
        self.label_number_of_cards.pack()

        # Create a button to draw a new card
        self.button_draw_card = tk.Button(
            self.root, text="Draw Development Card", command=self.draw_dev_card)
        self.button_draw_card.pack()

        # Add buttons for drawing outdoor and indoor tiles
        self.button_draw_outdoor_tile = tk.Button(
            self.root, text="Draw Outdoor Tile", command=self.draw_outdoor_tile)
        self.button_draw_outdoor_tile.pack()

        self.button_draw_indoor_tile = tk.Button(
            self.root, text="Draw Indoor Tile", command=self.draw_indoor_tile)
        self.button_draw_indoor_tile.pack()

        # Start the GUI main loop
        self.root.mainloop()

    def draw_outdoor_tile(self):
        tile = self.outdoor_tiles.draw()
        tile.display()
        tile_image = tile.image
        tile_tk_image = ImageTk.PhotoImage(tile_image)
        self.label_image.config(image=tile_tk_image)
        self.label_image.image = tile_tk_image

    def draw_indoor_tile(self):
        tile = self.indoor_tiles.draw()
        tile.display()
        tile_image = tile.image
        tile_tk_image = ImageTk.PhotoImage(tile_image)
        self.label_image.config(image=tile_tk_image)
        self.label_image.image = tile_tk_image

    def draw_dev_card(self):
        card = self.dev_cards.draw()
        card.print_content()

        card_image = card.image
        card_tk_image = ImageTk.PhotoImage(card_image)
        self.label_image.config(image=card_tk_image)
        self.label_image.image = card_tk_image

        # Update the label showing the number of cards remaining
        self.label_number_of_cards.config(
            text=f"Development Cards: {self.dev_cards.get_number_of_cards()}")
