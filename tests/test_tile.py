import unittest
from unittest.mock import patch
from tile import Tile


class TestTile(unittest.TestCase):

    @patch('PIL.Image.open')  # Mocking the Image.open function
    def setUp(self, MockImage):
        self._MockImage = MockImage
        self.tile = Tile(image=self._MockImage, name="Kitchen", exits={
                         "N": True, "S": False, "E": True, "W": True},
                         tile_type="indoor")

    def test_init(self):
        self.assertEqual(self.tile.image, self._MockImage)
        self.assertEqual(self.tile.name, "Kitchen")
        self.assertEqual(self.tile.exits, {
                         "N": True, "S": False, "E": True, "W": True})
        self.assertEqual(self.tile.tile_type, "indoor")

    def test_display(self):
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output
        self.tile.display()
        sys.stdout = sys.__stdout__
        self.assertTrue("Kitchen" in output.getvalue())

    def test_possible_exits(self):
        self.assertEqual(self.tile.possible_exits(), ['N', 'E', 'W'])

    def test_add_exit(self):
        self.tile.add_exit('S')
        self.assertTrue(self.tile.exits['S'])

    def test_rotate_N_E(self):
        self.tile.rotate('N', 'E')
        self.assertEqual(self.tile.exits, {
                         'N': True, 'S': True, 'E': False, 'W': True})

    def test_rotate_N_S(self):
        self.tile.rotate('N', 'S')
        self.assertEqual(self.tile.exits, {
                         'N': True, 'S': False, 'E': True, 'W': True})


if __name__ == '__main__':
    unittest.main()
