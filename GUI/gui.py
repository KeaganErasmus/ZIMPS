import tkinter as tk
from PIL import ImageTk


class GUI:
    """Displays the game board and player information.
    """

    def __init__(self, board_size=7, tile_size=120):
        self.root = tk.Tk()
        self.root.title("Zombie in my pocket")
        self.images = []
        cols, rows = board_size, board_size
        self.tile_size = tile_size
        self.player_row = 0
        self.player_col = 0

        self.canvas = tk.Canvas(
            self.root, width=self.tile_size * cols,
            height=self.tile_size * rows)
        self.canvas.pack()

        self.grid_rects = [[None for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                self.grid_rects[i][j] = self.canvas.create_rectangle(
                    j * self.tile_size, i * self.tile_size,
                    (j + 1) * self.tile_size, (i + 1) * self.tile_size)

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
        self.label_coords = tk.Label(self.root, text="N\nW\tE\nS")
        self.label_coords.pack()

    def place_tile(self, tile, row, col):
        tile_image = tile.image
        tile_image = tile_image.resize((self.tile_size, self.tile_size))
        tile_tk_image = ImageTk.PhotoImage(tile_image)
        self.canvas.create_image(
            col * self.tile_size, row * self.tile_size,
            image=tile_tk_image, anchor=tk.NW)
        self.images.append(tile_tk_image)

    def update_dev_cards(self, cards_count, current_time):
        self.label_time.config(text=f"Time: {current_time}")
        self.label_dev_cards.config(text=f"Development Cards: {cards_count}")

    def update_tile_count(self, indoor_count, outdoor_count):
        self.lable_outdoor_tiles.config(
            text=f"Outdoor Tiles: {outdoor_count}")
        self.lable_indoor_tiles.config(
            text=f"Indoor Tiles: {indoor_count}")

    def update_player_info(self, health, attack, items, location):
        self.lable_health.config(text=f"Health: {health}")
        self.lable_attack.config(text=f"Attack: {attack}")
        self.items.config(text=f"Items: {items}")
        self.move_player(*location)

    def move_player(self, row, col):
        self.player_row = row
        self.player_col = col
        self.draw_player()

    def draw_player(self):
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
