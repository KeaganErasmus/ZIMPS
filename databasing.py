import sqlite3
from sqlite3 import Error


class DataBasing:

    def __init__(self):
        self.conn = None
        self.cur = None

    def create_connection(self, db_file):
        """
        create a database connection to a SQLite database

        Sam
        """
        try:
            self.conn = sqlite3.connect(db_file)
            self.cur = self.conn.cursor()
            # print(sqlite3.version)
        except Error as e:
            print(e)

    def close_connection(self):
        """
        Sam
        """
        self.conn.close()

    def create_something(self, data):
        """
        Christian
        """
        self.cur.execute("CREATE TABLE IF NOT EXISTS data (text TEXT)")
        self.cur.execute(f"INSERT INTO data VALUES ('{str(data)}')")

    def read_from_db(self):
        """
        Keagan
        """
        rows = self.cur.execute("SELECT * FROM data").fetchall()
        return rows


if __name__ == '__main__':
    db = DataBasing()
    db.create_connection(r"db\database.db")
    db.create_something("string")
    db.read_from_db()
    db.close_connection()
