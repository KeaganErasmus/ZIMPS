from PIL import ImageTk, Image
import tkinter as tk


class GUI:
    """
    A graphical interface, mainly for testing the game logic.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Zombie in my pocket")
        self.images = []
        cols, rows = 7, 7  # Size of the grid
        self.tile_size = 120  # Size of each tile, in pixels

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
        self.label_number_of_cards = tk.Label(
            self.root, text=f"Development Cards: ")
        self.label_number_of_cards.pack()

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

    def update_dev_cards_count(self, count):
        self.label_number_of_cards.config(text=f"Development Cards: {count}")
