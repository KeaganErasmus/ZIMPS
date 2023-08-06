from PIL import Image
import random

IMAGE_PATH = 'assets/tiles.jpg'
INDOOR_TILES = {
    1: {'name': 'Bathroom', 'exits': {'N': True, 'S': False, 'E': False, 'W': False}},
    5: {'name': 'Family Room', 'exits': {'N': True, 'S': False, 'E': True, 'W': True}},
    2: {'name': 'Kitchen', 'exits': {'N': True, 'S': False, 'E': True, 'W': True}},
    6: {'name': 'Dining Room', 'exits': {'N': True, 'S': True, 'E': True, 'W': True}},
    3: {'name': 'Storage', 'exits': {'N': True, 'S': False, 'E': False, 'W': False}},
    7: {'name': 'Bedroom', 'exits': {'N': True, 'S': False, 'E': False, 'W': True}},
    4: {'name': 'Evil Temple', 'exits': {'N': False, 'S': False, 'E': True, 'W': True}},
    8: {'name': 'Foyer', 'exits': {'N': True, 'S': False, 'E': False, 'W': False}},
}

OUTDOOR_TILES = {
    1: {'name': 'Garden', 'exits': {'N': False, 'S': True, 'E': True, 'W': True}},
    5: {'name': 'Garage', 'exits': {'N': False, 'S': True, 'E': False, 'W': True}},
    2: {'name': 'Sitting Area', 'exits': {'N': False, 'S': True, 'E': True, 'W': True}},
    6: {'name': 'Patio', 'exits': {'N': True, 'S': True, 'E': True, 'W': False}},
    3: {'name': 'Yard', 'exits': {'N': False, 'S': True, 'E': True, 'W': True}},
    7: {'name': 'Yard', 'exits': {'N': False, 'S': True, 'E': True, 'W': True}},
    4: {'name': 'Graveyard', 'exits': {'N': False, 'S': True, 'E': True, 'W': False}},
    8: {'name': 'Yard', 'exits': {'N': False, 'S': True, 'E': True, 'W': True}},
}


class Tile:
    """
    A tile is a single square on the game board.
    """

    def __init__(self, image, name, exits):
        self.image = image
        self.name = name
        self.exits = exits

    def display(self):
        # self.image.show()
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

    def get_possible_exits(self):
        return [direction for direction, is_exit in self.exits.items() if is_exit]
    
    def rotate_tile_exits(self, chosen_entry, chosen_exit):
        """
        Rotate new tile to align the chosen entry with the chosen exit from the previous tile. Also rotate the tile's image.
        """
        print(f"chosen_exit: {chosen_exit}, chosen_entry: {chosen_entry}")
        rotations_needed = {'N': {'N': 2, 'E': 1, 'S': 0, 'W': 3},
                            'E': {'N': 3, 'E': 2, 'S': 3, 'W': 0},
                            'S': {'N': 0, 'E': 3, 'S': 2, 'W': 1},
                            'W': {'N': 1, 'E': 0, 'S': 1, 'W': 2}}[chosen_exit][chosen_entry]

        print(f"rotations_needed: {rotations_needed}")
        for _ in range(rotations_needed):
            self.exits = {'N': self.exits['W'], 'E': self.exits['N'], 
                            'S': self.exits['E'], 'W': self.exits['S']}
            self.image = self.image.rotate(-90)  # Rotate image 90 degrees counterclockwise
        
        return self


class TileDeck:
    """
    A tile deck is a collection of either indoor or outdoor tiles that can be drawn from.
    """

    def __init__(self, deck_type, image_path=IMAGE_PATH):
        self.tiles = []

        # Determine start row and metadata based on deck type
        start_row = 0 if deck_type == 'outdoor' else 2
        tile_metadata = OUTDOOR_TILES if deck_type == 'outdoor' else INDOOR_TILES

        image = Image.open(image_path)
        rows, cols = 4, 4
        tile_width = image.width // cols
        tile_height = image.height // rows
        index = 1

        for i in range(start_row, start_row + rows // 2):
            for j in range(cols):
                left = j * tile_width
                top = i * tile_height
                right = (j + 1) * tile_width
                bottom = (i + 1) * tile_height
                tile_image = image.crop((left, top, right, bottom))
                metadata = tile_metadata[index]
                tile = Tile(tile_image, metadata['name'], metadata['exits'])
                self.tiles.append(tile)
                index += 1
                
        random.shuffle(self.tiles)
        self.number_of_tiles = len(self.tiles)

    def draw_tile_by_name(self, name):
        for i, tile in enumerate(self.tiles):
            if tile.name == name:
                return self.tiles.pop(i)

    def draw(self):
        if self.tiles:
            tile = self.tiles.pop(0)
            self.number_of_tiles -= 1
            return tile

    def get_number_of_tiles(self):
        return self.number_of_tiles
