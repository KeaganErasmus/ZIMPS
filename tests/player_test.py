import unittest
from game import Game
from player import Player

the_game = Game()


class player_initial_stats(unittest.TestCase):
    def test_player_start_location(self):
        player_loc = the_game.player.get_location()
        print(player_loc)
        self.assertEqual(player_loc, (5, 3))

    def test_player_starting_health(self):
        player_health = the_game.player.health
        print(player_health)
        self.assertEqual(player_health, 6)

    def test_player_starting_attack(self):
        player_attack = the_game.player.attack
        print(player_attack)
        self.assertEqual(player_attack, 1)

    def test_player_starting_items(self):
        player_items = the_game.player.get_items()
        print(player_items)
        self.assertEqual(player_items, [])


if __name__ == '__main__':
    unittest.main()
