import unittest
from player import Player  # Assuming the Player class is in player.py


class TestPlayer(unittest.TestCase):
    def test_initialization_with_defaults(self):
        """Test Player initialization with default values."""
        player = Player(start_coordinates=(0, 0))
        self.assertEqual(player.location, (0, 0))
        self.assertEqual(player.health, 6)
        self.assertEqual(player.attack, 1)
        self.assertEqual(player.items, [])
        self.assertFalse(player.has_totem)

    def test_initialization_with_custom_values(self):
        """Test Player initialization with custom values."""
        player = Player(
            start_coordinates=(1, 1),
            health=10,
            attack=5,
            items=["sword", "shield"],
            has_totem=True,
        )
        self.assertEqual(player.location, (1, 1))
        self.assertEqual(player.health, 10)
        self.assertEqual(player.attack, 5)
        self.assertEqual(player.items, ["sword", "shield"])
        self.assertTrue(player.has_totem)

    def test_initialization_with_items_none(self):
        """Test initialization when items is explicitly set to None."""
        player = Player(start_coordinates=(0, 0), items=None)
        self.assertEqual(player.items, [])  # Ensure items defaults to an empty list

    def test_get_location(self):
        """Test get_location method."""
        player = Player(start_coordinates=(2, 3))
        self.assertEqual(player.get_location(), (2, 3))

    def test_get_attack(self):
        """Test get_attack method."""
        player = Player(start_coordinates=(0, 0), attack=4)
        self.assertEqual(player.get_attack(), 4)

    def test_get_items(self):
        """Test get_items method."""
        player = Player(start_coordinates=(0, 0), items=["potion"])
        self.assertEqual(player.get_items(), ["potion"])

    def test_get_health(self):
        """Test get_health method."""
        player = Player(start_coordinates=(0, 0), health=15)
        self.assertEqual(player.get_health(), 15)

    def test_take_damage(self):
        """Test take_damage method."""
        player = Player(start_coordinates=(0, 0), health=10)
        player.take_damage(3)
        self.assertEqual(player.health, 7)

    def test_take_totem(self):
        """Test take_totem method."""
        player = Player(start_coordinates=(0, 0))
        player.take_totem()
        self.assertTrue(player.has_totem)

    def test_get_details(self):
        """Test get_details method."""
        player = Player(
            start_coordinates=(1, 1),
            health=5,
            attack=3,
            items=["key", "map"],
        )
        expected_details = (
            "Location->(1, 1) \n"
            "Health->5 \n"
            "Attack->3 \n"
            "Items->['key', 'map']"
        )
        self.assertEqual(player.get_details(), expected_details)


if __name__ == "__main__":
    unittest.main()
