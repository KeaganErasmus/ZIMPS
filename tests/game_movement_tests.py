import unittest
from game import Game

the_game = Game()

class Test_player_moving(unittest.TestCase):
    def test_player_moving_n_from_foyer(self):
        # Player starting location is (x=5, y=3)
        # moving up takes away from x
        # eg (x=4, y=3)
        the_game.player_turn('n')
        self.assertEqual(the_game.player.get_location(), (4, 3))


    def test_player_moving_s_from_foyer(self):
        # Player starts in the foyer
        # it has 1 exit to the north
        # So player should not be able to move any other direction
        the_game.player.location = (5, 3)
        the_game._move_direction('S')
        self.assertEqual(the_game.player.location, (5, 3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
