from PIL import ImageTk, Image
import tkinter as tk

from cards import DevelopmentDeck
from tiles import TileDeck


class GUI:
    """
    A GUI for drawing cards from a deck.
    """

    def __init__(self):
        self.dev_deck = DevelopmentDeck('assets/dev_cards.jpg')
        self.outdoor_deck = TileDeck(
            'assets/tiles.jpg', rows=4, cols=4, start_row=0)
        self.indoor_deck = TileDeck(
            'assets/tiles.jpg', rows=4, cols=4, start_row=2)

        self.root = tk.Tk()
        self.root.title("Zombie in my pocket")

        # Create a blank placeholder image
        self.placeholder_image = Image.new('RGB', (345, 517), color='white')
        self.placeholder_tk_image = ImageTk.PhotoImage(self.placeholder_image)

        # Create a label to hold the card image and set the placeholder as the initial image
        self.label_image = tk.Label(self.root, image=self.placeholder_tk_image)
        self.label_image.image = self.placeholder_tk_image  # keep a reference
        self.label_image.pack()

        # Create a label to show the number of cards
        self.label_number_of_cards = tk.Label(
            self.root, text=f"Development Cards: {self.dev_deck.get_number_of_cards()}")
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
        tile = self.outdoor_deck.draw()
        tile_image = tile.image
        tile_tk_image = ImageTk.PhotoImage(tile_image)
        self.label_image.config(image=tile_tk_image)
        self.label_image.image = tile_tk_image

    def draw_indoor_tile(self):
        tile = self.indoor_deck.draw()
        tile_image = tile.image
        tile_tk_image = ImageTk.PhotoImage(tile_image)
        self.label_image.config(image=tile_tk_image)
        self.label_image.image = tile_tk_image

    def draw_dev_card(self):
        card = self.dev_deck.draw()
        card.print_content()

        card_image = card.image
        card_tk_image = ImageTk.PhotoImage(card_image)
        self.label_image.config(image=card_tk_image)
        self.label_image.image = card_tk_image

        # Update the label showing the number of cards remaining
        self.label_number_of_cards.config(
            text=f"Development Cards: {self.dev_deck.get_number_of_cards()}")
