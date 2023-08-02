from PIL import Image


class Tile:
    def __init__(self, image):
        self.image = image


class TileDeck:
    def __init__(self, image_path, rows, cols, start_row=0):
        self.tiles = []
        image = Image.open(image_path)
        tile_width = image.width // cols
        tile_height = image.height // rows

        for i in range(start_row, start_row + rows // 2):
            for j in range(cols):
                left = j * tile_width
                top = i * tile_height
                right = (j + 1) * tile_width
                bottom = (i + 1) * tile_height
                tile_image = image.crop((left, top, right, bottom))
                tile = Tile(tile_image)
                self.tiles.append(tile)

    def draw(self):
        return self.tiles.pop(0)
