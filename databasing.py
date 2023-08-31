import sqlite3
from sqlite3 import Error


class DataBasing:

    def __init__(self, db_file):
        """Initialize a new or connect to an existing database."""
        self.conn = self.create_connection(db_file)
        self.cur = self.conn.cursor()

    def create_connection(self, db_file):
        """Create a database connection to a SQLite database.
        Sam
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error: {e}")
            return None

    def close_connection(self):
        """Close the database connection.
        Sam
        """
        if self.conn:
            self.conn.close()

    def execute_query(self, query, data=None):
        """Execute a single query.
        Christian
        """
        try:
            if data:
                self.cur.execute(query, data)
            else:
                self.cur.execute(query)
            self.conn.commit()
        except Error as e:
            print(f"Error: {e}")

    def create_table(self, tbl_name, col_name, d_type):
        """Create a table with the given name, column, and data type.
        Christian
        """
        create_tbl_query = f"CREATE TABLE IF NOT EXISTS {tbl_name} ({col_name} {d_type})"
        self.execute_query(create_tbl_query)

    def insert_data(self, table_name, column_name, data):
        insert_data_query = f"INSERT INTO {table_name} ({column_name}) VALUES (?)"
        self.execute_query(insert_data_query, (data,))

    def read_from_db(self, table_name, column_name):
        read_query = f"SELECT {column_name} FROM {table_name}"
        rows = self.cur.execute(read_query).fetchall()
        return rows

    def delete_data(self, table_name, column_name, data):
        delete_data_query = f"DELETE FROM {table_name} WHERE {column_name} = ?"
        self.execute_query(delete_data_query, (data,))

    def update_data(self, table_name, column_name, old_data, new_data):
        update_data_query = f"UPDATE {table_name} SET {column_name} = ? WHERE {column_name} = ?"
        self.execute_query(update_data_query, (new_data, old_data))

    def add_column(self, table_name, new_column_name, data_type):
        """Add a new column to an existing table.
        """
        add_column_query = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {data_type}"
        self.execute_query(add_column_query)

    def search_data(self, table_name, column_name, search_text):
        search_query = f"SELECT * FROM {table_name} WHERE {column_name} LIKE ?"
        rows = self.cur.execute(search_query, (f"%{search_text}%",)).fetchall()
        return rows

    def drop_table(self, table_name):
        drop_table_query = f"DROP TABLE IF EXISTS {table_name}"
        self.execute_query(drop_table_query)

    def get_columns(self, table_name):
        self.cur.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in self.cur.fetchall()]
        return columns

    def bulk_insert(self, table_name, column_name, data_list):
        bulk_insert_query = f"INSERT INTO {table_name} ({column_name}) VALUES (?)"
        self.cur.executemany(bulk_insert_query, [
                             (data,) for data in data_list])
        self.conn.commit()


if __name__ == '__main__':
    db = DataBasing(r"db\database.db")

    # Create table
    db.create_table("players", "player_name", "TEXT")

    # Read data
    print(db.read_from_db("players", "player_name"))

    # Insert data
    db.insert_data("players", "player_name", "Chris")

    # Update data
    db.update_data("players", "player_name", "Chris", "Christian")
    print(db.read_from_db("players", "player_name"))

    # Bulk insert
    db.bulk_insert("players", "player_name", ["Sam", "Keagan", "Bob"])
    print(db.read_from_db("players", "player_name"))

    # Delete data
    db.delete_data("players", "player_name", "Sam")
    print(db.read_from_db("players", "player_name"))

    # Add column
    db.add_column("players", "player_age", "INTEGER")
    print(db.get_columns("players"))

    # Close connection
    db.close_connection()
