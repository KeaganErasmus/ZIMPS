import unittest
from tkinter import Tk
from GUI.gui import GUI


class TestGUI(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.gui = GUI()

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
        
    def test_update_player_info(self):
        self.gui.update_player_info(health=5, attack=2, items=["Chainsaw"], location=(1, 2))
        self.assertEqual(self.gui.lable_health.cget("text"), "Health: 5")
        self.assertEqual(self.gui.lable_attack.cget("text"), "Attack: 2")
        self.assertEqual(self.gui.items.cget("text"), "Items: ['Chainsaw']")
        self.assertEqual(self.gui.player_row, 1)
        self.assertEqual(self.gui.player_col, 2)

    def test_move_player(self):
        self.gui.move_player(1, 2)
        self.assertEqual(self.gui.player_row, 1)
        self.assertEqual(self.gui.player_col, 2)
        
    def test_player_marker_color(self):
        self.gui.draw_player()
        marker_color = self.gui.canvas.itemcget(self.gui.player_marker, "fill")
        self.assertEqual(marker_color, "red")
        

if __name__ == '__main__':
    unittest.main()
