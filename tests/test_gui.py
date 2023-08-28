import unittest
from tkinter import Tk
from GUI.gui import GUI
from board import Board


class TestGUI(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        # self.board = Board()
        self.gui = GUI(board_size=(7, 7), tile_size=120)

    def tearDown(self):
        self.root.quit()
        self.root.destroy()

    def test_initial_board(self):
        self.assertEqual(len(self.gui.grid_rects), 7)
        self.assertEqual(len(self.gui.grid_rects[0]), 7)

    def test_update_dev_cards(self):
        self.gui.update_dev_cards(cards_count=5, current_time="11 PM")
        self.assertEqual(self.gui.label_time.cget("text"), "Time: 11 PM")
        self.assertEqual(self.gui.label_dev_cards.cget("text"), "Development Cards: 5")

    def test_update_tile_count(self):
        self.gui.update_tile_count(indoor_count=3, outdoor_count=4)
        self.assertEqual(self.gui.lable_outdoor_tiles.cget("text"), "Outdoor Tiles: 4")
        self.assertEqual(self.gui.lable_indoor_tiles.cget("text"), "Indoor Tiles: 3")


if __name__ == '__main__':
    unittest.main()
