import unittest
from game import Game

the_game = Game()

class Test_player_moving(unittest.TestCase):
    def test_player_moving_n_from_foyer(self):
        # Player starting location is (x=5, y=3)
        # moving up takes away from x
        # eg (x=4, y=3)
        player_loc = ()
        turn = the_game.player_turn('n')
        if turn is None:
            player_loc = the_game.player.location
        else:
            # add logic to quit out of movement sequence
            pass
        self.assertEqual(player_loc, (4, 3))


    def test_player_moving_s_from_foyer(self):
        # Player starts in the foyer
        # it has 1 exit to the north
        # So player should not be able to move any other direction
        the_game.player.location = (5, 3)
        the_game._move_direction('S')
        self.assertEqual(the_game.player.location, (5, 3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
