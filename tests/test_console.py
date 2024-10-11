"""
Test document for console.py.

Run all tests individually.
"""
import unittest
from unittest.mock import MagicMock, patch
from console import Console


class TestConsole(unittest.TestCase):
    """TestConsole class for running all tests."""

    def setUp(self):
        """Do setup."""
        self.start_coordinates = (3, 3)
        self.board_size = (7, 7)
        self.card_data = 'assets/dev_cards.json'
        self.card_image = 'assets/dev_cards.jpg'

        self.console = Console(self.start_coordinates,
                               self.board_size,
                               self.card_data,
                               self.card_image)
        self.console.game = MagicMock()

        self.console.game.gui.root.mainloop()

    def test_do_go(self):
        """Test that do_go gets called with direction."""
        direction = 'N'

        with patch.object(self.console.game,
                          'check_game_state',
                          return_value=False):
            with patch.object(self.console.game,
                              'player_turn',
                              return_value=None) as mock_player_turn:
                self.console.do_go(direction)
                mock_player_turn.assert_called_once_with(direction)
                self.console.game.player_turn.assert_called_with(direction)

    def test_do_bash(self):
        """Test that do_bash gets called with direction."""
        direction = 'E'
        self.console.do_bash(direction)
        self.console.game.bash_through_wall.assert_called_with(direction)

    def test_do_totem(self):
        """Test that do_totem gets called."""
        self.console.do_totem(None)
        self.console.game.find_or_burry_totem.assert_called()

    def test_do_cower(self):
        """Test that do_cower gets called."""
        self.console.do_cower(None)
        self.console.game.cower.assert_called()

    def test_do_quit(self):
        """Test that do_quit gets called."""
        with patch('builtins.print') as mocked_print:
            self.console.do_quit(None)
            mocked_print.assert_called_with("Goodbye")
            self.console.game.gui.root.destroy.assert_called()

    def test_do_save(self):
        """Test that do_quit gets called."""
        self.console.do_save("save_file")
        self.console.game.save_game.assert_called()

    def test_do_shelve_save(self):
        """Test that do_quit gets called with filename."""
        self.console.do_shelve_save("shelve_file")
        self.console.game.shelve_save.assert_called_with("shelve_file")

    def test_do_json_save(self):
        """Test that do_quit gets called with filename."""
        self.console.do_json_save("json_file")
        self.console.game.json_save.assert_called_with("json_file")

    def test_do_load(self):
        """Test that do_load loads with filename."""
        filename = "player_data"
        self.console.do_load(filename)
        self.console.game.load_game.assert_called_with(filename)

    def test_do_shelve_load(self):
        """Test that do_shelve_load gets called with filename."""
        self.console.do_shelve_load("shelve_file")
        self.console.game.shelve_load.assert_called_with("shelve_file")

    def test_do_json_load(self):
        """Test that do_json_load gets called with filename."""
        self.console.do_json_load("json_file")
        self.console.game.json_load.assert_called_with("json_file")

    def test_do_details(self):
        """Test that do_details gets called."""
        self.console.do_details(None)
        self.console.game.get_details.assert_called()

    def test_do_coords(self):
        """Test that do_coords gets called."""
        with patch('builtins.print') as mocked_print:
            self.console.do_coords(None)
            mocked_print.assert_called_with("  N\nW\tE\n  S")


if __name__ == '__main__':
    unittest.main()
