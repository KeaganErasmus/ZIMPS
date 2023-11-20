import unittest
from unittest.mock import patch, MagicMock
from GameConfig import CustomGameConfig, CustomGameConfigFactory


class TestCustomGameConfig(unittest.TestCase):
    def setUp(self):
        self.config = CustomGameConfig()

    def test_default_values(self):
        args = self.config.parser.parse_args([])
        self.assertEqual(args.x, 5)
        self.assertEqual(args.y, 3)
        self.assertEqual(args.rows, 7)
        self.assertEqual(args.cols, 7)
        self.assertEqual(args.cards_data, 'assets/dev_cards.json')
        self.assertEqual(args.cards_image, 'assets/dev_cards.jpg')

    @patch('argparse.ArgumentParser.parse_args', return_value=MagicMock())
    @patch('sys.argv', ['program_name', '--x', '8', '--y', '3', '--rows', '5', '--cols', '5'])
    @patch('builtins.print')
    def test_parse_arguments_invalid_coordinates(self, mock_print, mock_parse_args):
        mock_args = MagicMock()
        mock_args.x, mock_args.y, mock_args.rows, mock_args.cols = 8, 3, 5, 5
        mock_parse_args.return_value = mock_args

        result = self.config.parse_arguments()
        mock_parse_args.assert_called_once_with()
        mock_print.assert_called_once_with("Invalid arguments: Coordinates (8, 3) Out of board bounds: (5, 5)")
        self.assertIsNone(result)

    @patch('sys.argv', ['program_name', '--x', '2', '--y', '3', '--rows', '5', '--cols', '5'])
    @patch('argparse.ArgumentParser.parse_args', return_value=MagicMock(x=2, y=3, rows=5, cols=5))
    def test_parse_arguments_valid_coordinates(self, mock_parse_args):
        result = self.config.parse_arguments()
        mock_parse_args.assert_called_once_with()
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 3)
        self.assertEqual(result.rows, 5)
        self.assertEqual(result.cols, 5)

    @patch('GameConfig.CustomGameConfigFactory.create_game_config', return_value=MagicMock(spec=CustomGameConfig))
    def test_create_game_config(self, mock_create_game_config):
        # Creating an instance of CustomGameConfigFactory
        factory = CustomGameConfigFactory()

        # Calling create_game_config on the factory
        config = factory.create_game_config()

        # Asserting that create_game_config is called once
        mock_create_game_config.assert_called_once()

        # Asserting that the returned value is an instance of CustomGameConfig
        self.assertIsInstance(config, CustomGameConfig)


if __name__ == '__main__':
    unittest.main()
