"""
Test document for console.py.
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

        # Mocking the game and its GUI components to avoid manual closing
        with patch('console.Game') as MockGame:
            self.console = Console(self.start_coordinates,
                                self.board_size,
                                self.card_data,
                                self.card_image)
            self.console.game = MockGame.return_value
            self.console.game.gui.root.mainloop = MagicMock()  # Mocking the GUI loop
            self.console.game.gui.root.destroy = MagicMock()   # Mocking GUI destroy

    def test_initialization(self):
        """Test that Console initializes properly and reads commands.txt."""
        with patch('console.open', unittest.mock.mock_open(read_data="go\nbash\n"), create=True) as mock_file:
            self.console = Console(self.start_coordinates, self.board_size, self.card_data, self.card_image)
            mock_file.assert_called_with("commands.txt", 'r')  

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

    def test_do_go_exception(self):
        """Test that do_go handles TypeError."""
        direction = 'N'
        with patch.object(self.console.game, 'check_game_state', return_value=False):
            with patch.object(self.console.game, 'player_turn', side_effect=TypeError("Invalid type")) as mock_player_turn:
                with patch('builtins.print') as mocked_print:
                    self.console.do_go(direction)
                    mocked_print.assert_called_with("Invalid type")
                    mock_player_turn.assert_called_once_with(direction) 

    def test_do_go_game_state_true(self):
        """Test that do_go exits when check_game_state is True."""
        direction = 'N'
        with patch.object(self.console.game, 'check_game_state', return_value=True):
            with patch.object(self.console.game, 'player_turn') as mock_player_turn:
                self.console.do_go(direction)
                mock_player_turn.assert_not_called()  # Ensures player_turn is not called if game state is True

    def test_do_bash(self):
        """Test that do_bash gets called with direction."""
        direction = 'E'
        self.console.do_bash(direction)
        self.console.game.bash_through_wall.assert_called_with(direction)

    def test_do_totem(self):
        """Test that do_totem gets called."""
        self.console.do_totem(None)
        self.console.game.find_or_burry_totem.assert_called()
    
    def test_do_totem_exception(self):
        """Test that do_totem handles TypeError."""
        with patch.object(self.console.game, 'find_or_burry_totem', side_effect=TypeError("Totem error")):
            with patch('builtins.print') as mocked_print:
                self.console.do_totem(None)
                mocked_print.assert_called_with("Totem error")

    def test_do_cower(self):
        """Test that do_cower gets called."""
        self.console.do_cower(None)
        self.console.game.cower.assert_called()

    def test_do_cower_exception(self):
        """Test that do_cower handles TypeError."""
        with patch.object(self.console.game, 'cower', side_effect=TypeError("Cower error")):
            with patch('builtins.print') as mocked_print:
                self.console.do_cower(None)
                mocked_print.assert_called_with("Cower error")

    def test_do_quit(self):
        """Test that do_quit ends the game properly."""
        with patch('builtins.print') as mocked_print:
            self.console.do_quit(None)
            mocked_print.assert_called_with("Goodbye")
            self.assertTrue(self.console.do_quit(None))

    def test_do_save(self):
        """Test that do_save gets called."""
        self.console.do_save("save_file")
        self.console.game.save_game.assert_called()

    def test_do_shelve_save(self):
        """Test that do_shelve_save gets called with filename."""
        self.console.do_shelve_save("shelve_file")
        self.console.game.shelve_save.assert_called_with("shelve_file")

    def test_do_shelve_save_no_filename(self):
        """Test that do_shelve_save handles missing filename."""
        # Mock shelve_save to raise an exception if no filename is passed
        with patch.object(self.console.game, 'shelve_save', side_effect=Exception):
            with patch('builtins.print') as mocked_print:
                self.console.do_shelve_save(None)  # Pass None to trigger the exception
                mocked_print.assert_called_with("Please enter a filename to save to")

    def test_do_json_save(self):
        """Test that do_json_save gets called with filename."""
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
