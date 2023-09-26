import unittest
import sqlite3
from databasing import DataBasing


class TestDataBasing(unittest.TestCase):

    def setUp(self):
        self.db = DataBasing(":memory:")  # Create a new database in memory
        self.db.create_table("players", "player_name", "TEXT")

    def tearDown(self):
        self.db.close_connection()

    def test_create_table(self):
        self.db.create_table("test_table", "test_col", "TEXT")
        cols = self.db.get_columns("test_table")
        self.assertIn("test_col", cols)

    def test_insert_data(self):
        self.db.insert_data("players", "player_name", "Chris")
        rows = self.db.read_from_db("players", "player_name")
        self.assertIn(("Chris",), rows)

    def test_update_data(self):
        self.db.insert_data("players", "player_name", "Chris")
        self.db.update_data("players", "player_name", "Chris", "Christian")
        rows = self.db.read_from_db("players", "player_name")
        self.assertIn(("Christian",), rows)
        self.assertNotIn(("Chris",), rows)

    def test_delete_data(self):
        self.db.insert_data("players", "player_name", "Chris")
        self.db.delete_data("players", "player_name", "Chris")
        rows = self.db.read_from_db("players", "player_name")
        self.assertNotIn(("Chris",), rows)

    def test_bulk_insert(self):
        self.db.bulk_insert("players", "player_name", ["Sam", "Keagan", "Bob"])
        rows = self.db.read_from_db("players", "player_name")
        self.assertEqual(len(rows), 3)

    def test_add_column(self):
        self.db.add_column("players", "player_age", "INTEGER")
        cols = self.db.get_columns("players")
        self.assertIn("player_age", cols)

    def test_search_data(self):
        self.db.insert_data("players", "player_name", "Sam")
        rows = self.db.search_data("players", "player_name", "Sam")
        self.assertIn(("Sam",), rows)

    def test_drop_table(self):
        self.db.drop_table("players")
        # Catch the error raised when table is missing
        with self.assertRaises(sqlite3.OperationalError):
            self.db.read_from_db("players", "player_name")


if __name__ == "__main__":
    unittest.main()
