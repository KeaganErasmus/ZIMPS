import unittest
from game import Game

the_game = Game()
class player_initial_stats(unittest.TestCase):
    def test_player_start_location(self):
        player_loc = the_game.player.location
        self.assertEqual(player_loc, (5, 3))  # add assertion here

    def test_player_starting_health(self):
        player_health = the_game.player.health
        self.assertEqual(player_health, 6)

    def test_player_starting_attack(self):
        player_attack = the_game.player.attack
        self.assertEqual(player_attack, 1)

    def test_player_starting_items(self):
        player_items = the_game.player.items
        self.assertEqual(player_items, [])


if __name__ == '__main__':
    unittest.main()
