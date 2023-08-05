from PIL import Image

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
    def __init__(self, image, name, exits):
        self.image = image
        self.name = name
        self.exits = exits

    def display(self):
        name_length = 15  # Set this to the length of the longest name
        # Center the name within the given length
        padded_name = self.name.center(name_length)

        top_exit = ' ' if self.exits['N'] else '_'
        right_exit = ' ' if self.exits['E'] else '|'
        bottom_exit = ' ' if self.exits['S'] else '_'
        left_exit = ' ' if self.exits['W'] else '|'

        print(f" {top_exit * (name_length + 2)} ")
        print(f"+{' ' * (name_length + 2)}+")
        print(f"{left_exit} {padded_name} {right_exit}")
        print(f"+{bottom_exit * (name_length + 2)}+")
        print('')


class TileDeck:
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

    def draw(self):
        return self.tiles.pop(0)
