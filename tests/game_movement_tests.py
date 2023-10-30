import unittest
from unittest.mock import patch
from game import Game

the_game = Game((5, 3), (7, 7), 'assets/dev_cards.json', 'assets/dev_cards.jpg')


class TestPlayerMoving(unittest.TestCase):
    def test_player_moving_n_from_foyer(self):
        with patch.object(the_game, '_move_direction') as mock_move_direction:
            the_game._move_direction.return_value = (4, 3)
            the_game.player_turn('n')
            player_loc = the_game.player.get_location()
            self.assertEqual(player_loc, (4, 3))
            mock_move_direction.assert_called_with('N')

    def test_player_moving_s_from_foyer(self):
        with patch.object(the_game, '_move_direction') as mock_move_direction:
            the_game._move_direction.return_value = (5, 3)
            turn = the_game._move_direction('S')
            self.assertEqual(turn, (5, 3))
            mock_move_direction.assert_called_with('S')

    def test_player_moving_w_from_foyer(self):
        with patch.object(the_game, '_move_direction') as mock_move_direction:
            the_game._move_direction.return_value = None
            turn = the_game._move_direction('W')
            self.assertEqual(turn, None)
            mock_move_direction.assert_called_with('W')

    def test_player_moving_e_from_foyer(self):
        with patch.object(the_game, '_move_direction') as mock_move_direction:
            the_game._move_direction.return_value = None
            turn = the_game._move_direction('E')
            self.assertEqual(turn, None)
            mock_move_direction.assert_called_with('E')


if __name__ == '__main__':
    unittest.main()
