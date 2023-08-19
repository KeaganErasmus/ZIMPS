import tkinter as tk
from PIL import ImageTk


class GUI:
    """
    A graphical interface displaying the game board and development cards.
    """

    def __init__(self, board_size=7, tile_size=100):
        self.root = tk.Tk()
        self.root.title("Zombie in my pocket")
        self.images = []  # A list to store references to the tile images
        cols, rows = board_size, board_size
        self.tile_size = tile_size  # The size of each tile in pixels

        # Create a canvas to hold the tiles
        self.canvas = tk.Canvas(
            self.root, width=self.tile_size*cols, height=self.tile_size*rows)
        self.canvas.pack()

        # Create a grid of squares on the canvas
        self.grid_rects = [[None for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                self.grid_rects[i][j] = self.canvas.create_rectangle(
                    j*self.tile_size, i*self.tile_size, (j+1)*self.tile_size, (i+1)*self.tile_size)

        # Create labels to show the number of cards and tiles remaining
        self.label_time = tk.Label(
            self.root, text="Time: ")
        self.label_time.pack()

        self.label_dev_cards = tk.Label(
            self.root, text="Development Cards: ")
        self.label_dev_cards.pack()

        self.lable_outdoor_tiles = tk.Label(
            self.root, text="Outdoor Tiles: ")
        self.lable_outdoor_tiles.pack()

        self.lable_indoor_tiles = tk.Label(
            self.root, text="Indoor Tiles: ")
        self.lable_indoor_tiles.pack()

        self.lable_health = tk.Label(
            self.root, text="Health: ")
        self.lable_health.pack()

        self.lable_attack = tk.Label(
            self.root, text="Attack: ")
        self.lable_attack.pack()

        self.items = tk.Label(
            self.root, text="Items: ")
        self.items.pack()

    def place_tile(self, tile, row, col):
        tile_image = tile.image
        # Resize the image to fit the tile size
        tile_image = tile_image.resize((self.tile_size, self.tile_size))
        tile_tk_image = ImageTk.PhotoImage(tile_image)
        # Use the create_image method to draw the image on the canvas
        self.canvas.create_image(
            col*self.tile_size, row*self.tile_size, image=tile_tk_image, anchor=tk.NW)
        # Add this line to store a reference to the image
        self.images.append(tile_tk_image)

    def update_dev_cards(self, cards_count, current_time):
        self.label_time.config(text=f"Time: {current_time}")
        self.label_dev_cards.config(text=f"Development Cards: {cards_count}")

    def update_tile_count(self, indoor_count, outdoor_count):
        self.lable_outdoor_tiles.config(text=f"Outdoor Tiles: {outdoor_count}")
        self.lable_indoor_tiles.config(text=f"Indoor Tiles: {indoor_count}")

    def update_player_info(self, health, attack, items):
        self.lable_health.config(text=f"Health: {health}")
        self.lable_attack.config(text=f"Attack: {attack}")
        self.items.config(text=f"Items: {items}")
