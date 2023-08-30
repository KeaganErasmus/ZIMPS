import unittest
from unittest import mock
from GUI.gui import GUI


class TestPlaceTile(unittest.TestCase):

    @mock.patch('tkinter.Canvas')
    @mock.patch('PIL.ImageTk.PhotoImage')
    @mock.patch('tile.Tile')
    def test_place_tile(self, MockTile, MockPhotoImage, MockCanvas):
        # Setup
        gui = GUI()
        gui.canvas = MockCanvas()
        mock_tile = MockTile()
        mock_tile.image = MockPhotoImage()
        row = 1
        col = 2

        # Act
        gui.place_tile(mock_tile, row, col)

        # Assert
        mock_tile.image.resize.assert_called_with(
            (gui.tile_size, gui.tile_size))

        gui.canvas.create_image.assert_called_with(
            col * gui.tile_size, row * gui.tile_size,
            image=mock_tile.image, anchor='nw')

        self.assertEqual(len(gui.images), 1)
        self.assertEqual(gui.images[-1], mock_tile.image)


if __name__ == '__main__':
    unittest.main()
