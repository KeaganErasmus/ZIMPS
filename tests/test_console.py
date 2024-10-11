import unittest
from unittest.mock import patch, MagicMock
from console import Console  # Adjust this import based on your file structure
from game import Game

class TestConsole(unittest.TestCase):

    def setUp(self):
        # Set up a Console instance before each test
        start_coordinates = (0, 0)
        board_size = (5, 5)
        card_data = "sample_card_data"
        card_image = "sample_card_image"
        
        # Mock the Game class
        self.mock_game = MagicMock(spec=Game)
        self.console = Console(start_coordinates, board_size, card_data, card_image)
        self.console.game = self.mock_game

    def test_do_go_success(self):
        self.mock_game.check_game_state.return_value = False
        self.console.do_go('N')
        self.mock_game.player_turn.assert_called_with('N')

    def test_do_go_invalid_direction(self):
        self.mock_game.check_game_state.return_value = False
        self.mock_game.player_turn.side_effect = TypeError("Invalid direction")
        
        with patch('builtins.print') as mocked_print:
            self.console.do_go('X')
            mocked_print.assert_called_once_with("Invalid direction")

    def test_do_bash(self):
        self.console.do_bash('N')
        self.mock_game.bash_through_wall.assert_called_with('N')

    def test_do_totem(self):
        self.mock_game.find_or_burry_totem = MagicMock()
        self.console.do_totem(None)
        self.mock_game.find_or_burry_totem.assert_called_once()

    def test_do_cower(self):
        self.mock_game.cower = MagicMock()
        self.console.do_cower(None)
        self.mock_game.cower.assert_called_once()

    def test_do_quit(self):
        with patch('builtins.print') as mocked_print:
            self.console.do_quit(None)
            mocked_print.assert_called_once_with("Goodbye")
            self.mock_game.gui.root.destroy.assert_called_once()

    def test_do_save(self):
        self.console.do_save('test_save')
        self.mock_game.save_game.assert_called_once()

    def test_do_shelve_save(self):
        self.console.do_shelve_save('test_shelve_save')
        self.mock_game.shelve_save.assert_called_once_with('test_shelve_save')

    def test_do_shelve_load(self):
        self.console.do_shelve_load('test_shelve_load')
        self.mock_game.shelve_load.assert_called_once_with('test_shelve_load')

    def test_do_json_save(self):
        self.console.do_json_save('test_json_save')
        self.mock_game.json_save.assert_called_once_with('test_json_save')

    def test_do_json_load(self):
        self.console.do_json_load('test_json_load')
        self.mock_game.json_load.assert_called_once_with('test_json_load')

    def test_do_load(self):
        self.console.do_load('test_load')
        self.mock_game.load_game.assert_called_once_with('test_load')

    def test_do_details(self):
        self.console.do_details(None)
        self.mock_game.get_details.assert_called_once()

    def test_do_coords(self):
        with patch('builtins.print') as mocked_print:
            self.console.do_coords(None)
            mocked_print.assert_called_once_with("  N\nW\tE\n  S")

if __name__ == "__main__":
    unittest.main()
