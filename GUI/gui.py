# --------------------------------------------------------------
# gui.py
# --------------------------------------------------------------
# Author: Christian Diekmann
#
# Description:
# A GUI for the Zombie in my Pocket game.
# ---------------------------------------------------------------
import io
import tkinter as tk
from PIL import ImageTk, Image


class GUI:
    """Displays the game board and player information.
    """

    def __init__(self, board_size=(7, 7), tile_size=120):
        self.root = tk.Tk()
        self.root.title("Zombie in my pocket")
        self.images = []
        cols, rows = board_size
        self.tile_size = tile_size
        self.player_row = 0
        self.player_col = 0

        # Create a main frame to hold the lables
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        # Create a frame to contain the Canvas
        self.canvas_frame = tk.Frame(self.main_frame)
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add a canvas to the canvas frame
        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Create scrollbars for the canvas
        self.scrollbar_y = tk.Scrollbar(
            self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar_x = tk.Scrollbar(
            self.main_frame, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.canvas.configure(
            yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Add widgets to the  the root window
        self.frame_group1 = tk.Frame(self.root)
        self.frame_group1.pack(side=tk.LEFT, padx=20)

        self.frame_group2 = tk.Frame(self.root)
        self.frame_group2.pack(side=tk.LEFT, padx=60)

        self.label_time = tk.Label(self.frame_group1, text="Time: ")
        self.label_time.pack()
        self.label_dev_cards = tk.Label(
            self.frame_group1, text="Development Cards: ")
        self.label_dev_cards.pack()

        self.lable_outdoor_tiles = tk.Label(
            self.frame_group1, text="Outdoor Tiles: ")
        self.lable_outdoor_tiles.pack()
        self.lable_indoor_tiles = tk.Label(
            self.frame_group1, text="Indoor Tiles: ")
        self.lable_indoor_tiles.pack()

        self.lable_health = tk.Label(self.frame_group2, text="Health: ")
        self.lable_health.pack()
        self.lable_attack = tk.Label(self.frame_group2, text="Attack: ")
        self.lable_attack.pack()
        self.items = tk.Label(self.frame_group2, text="Items: ")
        self.items.pack()

        # self.frame_compass = tk.Frame(self.root)
        # self.frame_compass.pack(side=tk.LEFT, padx=80)
        # self.compass_image = self._load_image("../GUI/compass.png", (80, 80))
        # if self.compass_image is None:
        #     raise Exception("Compass image not found.")
        # self.compass_label = tk.Label(
        #     self.frame_compass, image=self.compass_image)
        # self.compass_label.pack()

        # Create another frame INSIDE the canvas
        self.frame_inside_canvas = tk.Frame(self.canvas)

        # Add that inner frame to a window in the canvas
        self.canvas.create_window(
            (0, 0), window=self.frame_inside_canvas, anchor="nw")

        self.grid_rects = [[None for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                self.grid_rects[i][j] = self.canvas.create_rectangle(
                    j * self.tile_size, i * self.tile_size,
                    (j + 1) * self.tile_size, (i + 1) * self.tile_size)

        # Update the scrollregion of the canvas to encompass the inner frame
        self.frame_inside_canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Bind the mouse scroll event to scrolling function
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Shift-MouseWheel>", self._on_shiftmousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1*(event.delta//120), "units")

    def _on_shiftmousewheel(self, event):
        self.canvas.xview_scroll(-1*(event.delta//120), "units")

    def place_tile(self, tile, row, col):
        """Places a tile on the board at the given row and column.
        """
        tile_image = tile.image
        tile_image = tile_image.resize((self.tile_size, self.tile_size))
        tile_tk_image = ImageTk.PhotoImage(tile_image)
        self.canvas.create_image(
            col * self.tile_size, row * self.tile_size,
            image=tile_tk_image, anchor=tk.NW)
        self.images.append(tile_tk_image)

    def update_dev_cards(self, cards_count, current_time):
        """Updates the development cards and time labels.
        """
        self.label_time.config(text=f"Time: {current_time}")
        self.label_dev_cards.config(text=f"Development Cards: {cards_count}")

    def update_tile_count(self, indoor_count, outdoor_count):
        """Updates the indoor and outdoor tile count labels.
        """
        self.lable_outdoor_tiles.config(
            text=f"Outdoor Tiles: {outdoor_count}")
        self.lable_indoor_tiles.config(
            text=f"Indoor Tiles: {indoor_count}")

    def update_player_info(self, health, attack, items, location):
        """Updates the player information labels and moves the player marker.
        """
        self.lable_health.config(text=f"Health: {health}")
        self.lable_attack.config(text=f"Attack: {attack}")
        self.items.config(text=f"Items: {items}")
        self._move_player(*location)

    def _move_player(self, row, col):
        """Moves the player marker to the given row and column.
        """
        self.player_row = row
        self.player_col = col
        self._draw_player()

    def _draw_player(self):
        """Draws the player marker on the board.
        """
        # Remove the previous player marker (if it exists)
        if hasattr(self, 'player_marker'):
            self.canvas.delete(self.player_marker)

        # Calculate the size of the marker as one-eighth the tile size
        marker_size = self.tile_size // 8

        # Draw a new marker at the player's current position
        self.player_marker = self.canvas.create_oval(
            self.player_col * self.tile_size + 3 * marker_size,
            self.player_row * self.tile_size + 3 * marker_size,
            (self.player_col + 1) * self.tile_size - 3 * marker_size,
            (self.player_row + 1) * self.tile_size - 3 * marker_size,
            fill="red")

    def _load_image(self, path, dimensions):
        """Loads an image from the given path and resizes it to the given
        dimensions.
        """
        try:
            image = Image.open(path)
            image = image.resize(dimensions)
            tk_image = ImageTk.PhotoImage(image)
            return tk_image

        except Exception as e:
            print(f"Error: {e}")
            return None

    def save_canvas_as_image(self, filename):
        """Saves the canvas as an image with the given filename.
        """
        try:
            # Saving the canvas in PostScript format
            ps = self.canvas.postscript(colormode='color')

            # Converting PostScript format to desired image format using PIL
            image = Image.open(io.BytesIO(ps.encode('utf-8')))
            image.save(filename)

        except Exception as e:
            print(f"Error while saving the canvas image: {e}")
