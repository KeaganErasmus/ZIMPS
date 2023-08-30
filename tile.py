# --------------------------------------------------------------
# tile.py
# --------------------------------------------------------------
# Author: Christian Diekmann
#
# Description:
# A tile is a single square on the game board.
# It has a name, an image, and exits to other tiles.
# Also has a tile type, either 'indoor' or 'outdoor'.
# ---------------------------------------------------------------
class Tile:
    """
    A tile is a single square on the game board.
    """

    def __init__(self, image, name, exits, tile_type):
        self.image = image
        self.name = name
        self.exits = exits
        self.tile_type = tile_type  # 'indoor' or 'outdoor'

    def display(self):
        """
        Display the tile name and exits in a nice ASCII art format.
        """
        max_name_len = 15  # Set this to the length of the longest name
        padded_name = self.name.center(max_name_len)  # Center the name

        top_exit = ' ' if self.exits['N'] else '_'
        right_exit = ' ' if self.exits['E'] else '|'
        bottom_exit = ' ' if self.exits['S'] else '_'
        left_exit = ' ' if self.exits['W'] else '|'

        print(f" {top_exit * (max_name_len + 2)} ")
        print(f"+{' ' * (max_name_len + 2)}+")
        print(f"{left_exit} {padded_name} {right_exit}")
        print(f"+{bottom_exit * (max_name_len + 2)}+")
        print('')

    def possible_exits(self):
        """
        List of possible exits from the tile.
        """
        return [d for d, is_exit in self.exits.items() if is_exit]

    def add_exit(self, direction):
        """
        Add an exit in the given direction to the tile.
        """
        self.exits[direction] = True

    def rotate(self, entry, exit):
        """
        Rotate tile to align the chosen entry with the chosen exit.
        """
        rotations = {'N': {'N': 2, 'E': 1, 'S': 0, 'W': 3},
                     'E': {'N': 3, 'E': 2, 'S': 1, 'W': 0},
                     'S': {'N': 0, 'E': 3, 'S': 2, 'W': 1},
                     'W': {'N': 1, 'E': 0, 'S': 3, 'W': 2}
                     }[exit][entry]

        for _ in range(rotations):
            self.exits = {direction: self.exits[prev_dir]
                          for direction, prev_dir in zip('NESW', 'WNES')}
            self.image = self.image.rotate(-90)

        return self
