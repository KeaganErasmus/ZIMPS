import unittest
from unittest.mock import MagicMock, patch
from console_strategy import Console  # Make sure you import from console_strategy


class TestConsoleStrategy(unittest.TestCase):
    """TestConsoleStrategy class for running all tests."""

    def setUp(self):
        """Do setup."""
        self.start_coordinates = (3, 3)
        self.board_size = (7, 7)
        self.card_data = 'assets/dev_cards.json'
        self.card_image = 'assets/dev_cards.jpg'

        # Mocking the game and its GUI components to avoid manual closing
        with patch('console_strategy.Game') as MockGame:
            self.console = Console(self.start_coordinates,
                                   self.board_size,
                                   self.card_data,
                                   self.card_image)
            self.console.game = MockGame.return_value
            self.console.game.gui.root.mainloop = MagicMock()  # Mocking the GUI loop
            self.console.game.gui.root.destroy = MagicMock()  # Mocking GUI destroy

        # Mocking strategies to ensure actions can be executed
        self.console.strategies = {
            "go": MagicMock(),
            "bash": MagicMock(),
            "totem": MagicMock(),
            "cower": MagicMock(),
            "quit": MagicMock(),
            "save": MagicMock(),
            "load": MagicMock(),
            "shelve_save": MagicMock(),
            "shelve_load": MagicMock(),
            "json_save": MagicMock(),
            "json_load": MagicMock(),
            "details": MagicMock(),
            "coords": MagicMock(),
        }

    def test_initialization(self):
        """Test that Console initializes properly and reads commands.txt."""
        with patch('builtins.open', unittest.mock.mock_open(read_data="go\nbash\n"), create=True) as mock_file:
            self.console = Console(self.start_coordinates, self.board_size, self.card_data, self.card_image)
            mock_file.assert_called_with("commands.txt", 'r')

    def test_do_go(self):
        """Test that do_go calls do_action with the correct parameters."""
        direction = 'N'
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_go(direction)
            mock_do_action.assert_called_once_with("go", direction)

    def test_do_bash(self):
        """Test that do_bash calls do_action with the correct parameters."""
        direction = 'E'
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_bash(direction)
            mock_do_action.assert_called_once_with("bash", direction)

    def test_do_totem(self):
        """Test that do_totem calls do_action with the correct parameters."""
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_totem(None)
            mock_do_action.assert_called_once_with("totem", None)

    def test_do_cower(self):
        """Test that do_cower calls do_action with the correct parameters."""
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_cower(None)
            mock_do_action.assert_called_once_with("cower", None)

    def test_do_quit(self):
        """Test that do_quit calls do_action with the correct parameters."""
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_quit(None)
            mock_do_action.assert_called_once_with("quit", None)

    def test_do_save(self):
        """Test that do_save calls do_action with the correct parameters."""
        self.console.do_save("save_file")
        self.console.strategies["save"].execute.assert_called_with(self.console.game, "save_file")

    def test_do_load(self):
        """Test that do_load calls do_action with the correct parameters."""
        self.console.do_load("load_file")
        self.console.strategies["load"].execute.assert_called_with(self.console.game, "load_file")

    def test_do_shelve_save(self):
        """Test that do_shelve_save calls do_action with the correct parameters."""
        filename = "shelve_file"
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_shelve_save(filename)
            mock_do_action.assert_called_once_with("shelve_save", filename)

    def test_do_shelve_load(self):
        """Test that do_shelve_load calls do_action with the correct parameters."""
        filename = "shelve_file"
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_shelve_load(filename)
            mock_do_action.assert_called_once_with("shelve_load", filename)

    def test_do_json_save(self):
        """Test that do_json_save calls do_action with the correct parameters."""
        filename = "json_file"
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_json_save(filename)
            mock_do_action.assert_called_once_with("json_save", filename)

    def test_do_json_load(self):
        """Test that do_json_load calls do_action with the correct parameters."""
        filename = "json_file"
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_json_load(filename)
            mock_do_action.assert_called_once_with("json_load", filename)

    def test_do_details(self):
        """Test that do_details calls do_action with the correct parameters."""
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_details(None)
            mock_do_action.assert_called_once_with("details")

    def test_do_coords(self):
        """Test that do_coords calls do_action with the correct parameters."""
        with patch.object(self.console, 'do_action') as mock_do_action:
            self.console.do_coords(None)
            mock_do_action.assert_called_once_with("coords")

    def test_do_action_valid_strategy(self):
        """Test that do_action correctly calls execute on the valid strategy."""
        action = "go"  # Valid action
        direction = "N"
        
        # Ensure the strategy is called with the correct parameters
        self.console.do_action(action, direction)
        self.console.strategies[action].execute.assert_called_once_with(self.console.game, direction)

    def test_do_action_invalid_strategy(self):
        """Test that do_action prints an error for an invalid strategy."""
        action = "invalid_action"  # Invalid action not in strategies
        direction = "N"
        
        with patch('builtins.print') as mock_print:  # Mock print to check for error message
            self.console.do_action(action, direction)
            mock_print.assert_called_with(f"Unknown action: {action}")  # Ensure "Unknown action" is printed

if __name__ == '__main__':
    unittest.main()
