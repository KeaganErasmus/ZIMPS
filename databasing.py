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

    def create_table(self):
        """Create a table.
        Christian
        """
        create_table_query = "CREATE TABLE IF NOT EXISTS data (text TEXT)"
        self.execute_query(create_table_query)

    def insert_data(self, data):
        """Insert new data into table.
        Christian
        """
        insert_data_query = "INSERT INTO data (text) VALUES (?)"
        self.execute_query(insert_data_query, (data,))

    def read_from_db(self):
        """Read all rows from database.
        Keagan
        """
        read_query = "SELECT * FROM data"
        rows = self.cur.execute(read_query).fetchall()
        return rows

    def delete_data(self, data):
        """Delete data from table.
        Keagan
        """
        delete_data_query = "DELETE FROM data WHERE text = ?"
        self.execute_query(delete_data_query, (data,))

    def update_data(self, old_data, new_data):
        """Update data in the table.
        Sam
        """
        update_data_query = "UPDATE data SET text = ? WHERE text = ?"
        self.execute_query(update_data_query, (new_data, old_data))


if __name__ == '__main__':
    db = DataBasing(r"db\database.db")

    # Create table
    db.create_table()

    # Insert data
    db.insert_data("string")
    print(db.read_from_db())

    # Delete data
    db.delete_data("string")
    print(db.read_from_db())

    # Update data
    db.insert_data("string")
    print(db.read_from_db())
    db.update_data("string", "new_string")
    print(db.read_from_db())

    # Close connection
    db.close_connection()
