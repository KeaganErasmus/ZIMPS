import unittest
from tile_deck import IndoorTiles


class TestTileDeck(unittest.TestCase):

    def setUp(self):
        self.tile_deck = IndoorTiles()

    def test_init(self):
        self.assertIsNotNone(self.tile_deck.tiles)
        self.assertEqual(self.tile_deck.count, len(self.tile_deck.tiles))

    def test_draw(self):
        initial_count = self.tile_deck.count
        tile = self.tile_deck.draw()
        self.assertIsNotNone(tile)
        self.assertEqual(self.tile_deck.count, initial_count - 1)

    def test_draw_by_name(self):
        tile = self.tile_deck.draw_by_name("Bathroom")
        self.assertIsNotNone(tile)
        self.assertEqual(tile.name, "Bathroom")

    def test_draw_empty_deck(self):
        self.tile_deck.tiles = []
        self.tile_deck.count = 0
        tile = self.tile_deck.draw()
        self.assertIsNone(tile)


if __name__ == '__main__':
    unittest.main()
