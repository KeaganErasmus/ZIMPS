import unittest
from game import Game

the_game = Game()
class MyTestCase(unittest.TestCase):
    def test_player_start_location(self):
        player_loc = the_game.player.location

        self.assertEqual(player_loc == (5, 3), True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
