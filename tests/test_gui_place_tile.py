import unittest
from unittest import mock
from GUI.gui import GUI


class TestPlaceTile(unittest.TestCase):

    @mock.patch('tkinter.Canvas')
    @mock.patch('PIL.ImageTk.PhotoImage')
    def test_place_tile(self, MockPhotoImage, MockCanvas):
        
        gui = GUI()
        gui.canvas = MockCanvas()
        mock_tile = mock.Mock()
        mock_tile.image = mock.Mock()

        # Call method to test
        gui.place_tile(mock_tile, 1, 2)
               
        # Check if image is resized
        mock_tile.image.resize.assert_called_with((gui.tile_size, gui.tile_size))

        # Check if create_image is called on the canvas
        gui.canvas.create_image.assert_called()

        # Check if image is appended to self.images
        self.assertIsInstance(gui.images[-1], mock.MagicMock)


if __name__ == '__main__':
    unittest.main()