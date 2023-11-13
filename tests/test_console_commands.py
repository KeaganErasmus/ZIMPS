import unittest
from io import StringIO
from unittest.mock import patch

from game import Game
from console import Console
from player import Player


class TestConsoleCommands(unittest.TestCase):

    def setUp(self):
        self.start_coordinates = (0, 0)
        self.board_size = (5, 5)
        self.card_data = 'assets/dev_cards.json'
        self.card_image = 'assets/dev_cards.jpg'
        self.console = Console(self.start_coordinates, self.board_size, self.card_data, self.card_image)
        self.player = Player(self.start_coordinates)

    def tearDown(self):
        if hasattr(self.console.game.gui, 'root'):
            self.console.game.gui.root.destroy()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, function, *args):
        function(*args)
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    def test_do_go_successful(self):
        # Test the do_go method with a successful move
        with patch.object(self.console.game, 'check_game_state', return_value=False):
            with patch.object(self.console.game, 'player_turn', return_value=None) as mock_player_turn:
                self.console.do_go('N')
                mock_player_turn.assert_called_once_with('N')

    def test_do_bash(self):
        # Test the do_bash method
        with patch.object(self.console.game, 'bash_through_wall', return_value=None) as mock_bash:
            self.console.do_bash('E')
            mock_bash.assert_called_once_with('E')

    def test_do_totem(self):
        # Test the do_totem method
        with patch.object(self.console.game, 'find_or_burry_totem', return_value=None) as mock_totem:
            self.console.do_totem('')
            mock_totem.assert_called_once()

    def test_do_totem_exception(self):
        # Test the do_totem method when a TypeError occurs
        with patch.object(self.console.game, 'find_or_burry_totem', side_effect=TypeError("Test error")):
            with patch('builtins.print') as mock_print:
                self.console.do_totem('')
                mock_print.assert_called_once_with("Test error")

    def test_do_cower(self):
        # Test the do_cower method
        with patch.object(self.console.game, 'cower', return_value=None) as mock_cower:
            self.console.do_cower('N')
            mock_cower.assert_called_once()

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_cower_exception(self, mock_stdout):
        # Test the do_cower method exception handling
        with patch.object(self.console.game, 'cower', side_effect=TypeError("Test error")):
            self.console.do_cower('')
            expected_output = "Test error"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_do_quit(self):
        # Test the do_quit method
        with patch('builtins.print') as mock_print:
            with patch.object(self.console.game.gui.root, 'destroy', return_value=None) as mock_destroy:
                result = self.console.do_quit('')
                mock_print.assert_called_once_with("Goodbye")
                mock_destroy.assert_called_once()
                self.assertTrue(result)

    def test_do_save(self):
        # Test the do_save method
        with patch.object(self.console.game, 'save_game', return_value=None) as mock_save_game:
            self.console.do_save('filename')
            mock_save_game.assert_called_once()

    @patch.object(Game, 'load_game')
    def test_do_load(self, mock_json_load):
        # Test the do_json_load method
        filename = 'test_file.txt'
        self.console.do_load(filename)
        mock_json_load.assert_called_once_with(filename)

    def test_do_shelve_save(self):
        # Test the do_shelve_save method
        with patch.object(self.console.game, 'shelve_save', return_value=None) as mock_shelve_save:
            self.console.do_shelve_save('filename_shelve')
            mock_shelve_save.assert_called_once_with('filename_shelve')
            self.console.do_shelve_load('filename_shelve')

    def test_do_shelve_save_exception(self):
        # Test the do_shelve_save method when an exception occurs
        with patch.object(self.console.game, 'shelve_save', side_effect=Exception("Test error")):
            with patch('builtins.print') as mock_print:
                self.console.do_shelve_save('')
                mock_print.assert_called_once_with("Please enter a filename to save to")

    def test_do_json_save(self):
        # Test the do_json_save method
        with patch.object(self.console.game, 'json_save', return_value=None) as mock_json_save:
            self.console.do_json_save('filename')
            mock_json_save.assert_called_once_with('filename')

    @patch.object(Game, 'json_load')
    def test_do_json_load(self, mock_json_load):
        # Test the do_json_load method
        filename = 'test_file.json'
        self.console.do_json_load(filename)
        mock_json_load.assert_called_once_with(filename)

    @patch('game.Game.get_details',
           return_value=f"Location->(0, 0)\nHealth->6\nAttack->1\nItems->[]\nTotem->False")
    def test_do_details(self, mock_get_details):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.do_details('')
            expected_output = (f"Location->{self.player.get_location()}"
                               f"\nHealth->{self.player.get_health()}"
                               f"\nAttack->{self.player.get_attack()}"
                               f"\nItems->{self.player.get_items()}"
                               f"\nTotem->{self.player.has_totem}")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_coords(self, mock_stdout):
        # Test the do_coords method
        self.console.do_coords('')
        expected_output = "N\nW\tE\n  S"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
