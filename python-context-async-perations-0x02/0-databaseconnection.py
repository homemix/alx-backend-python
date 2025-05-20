import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        if self.conn is not None:
            self.cursor = self.conn.cursor()
        else:
            self.cursor = None
            print(f" DB Connection: {self.db_name} error")

        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()


with DatabaseConnection("users.db") as db:
    db.execute("SELECT * FROM users")
    rows = db.fetchall()
    for row in rows:
        print(row)
