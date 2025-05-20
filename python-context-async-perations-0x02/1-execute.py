import sqlite3


class ExecuteQuery:
    def __init__(self, query):
        self.query = query
        self.parameter = (25,)
        self.db_name = "users.db"
        self.result = []

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query,self.parameter)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


with ExecuteQuery(query="SELECT * FROM users WHERE age > ?") as results:
    for row in results:
        print(row)
