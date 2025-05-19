import sqlite3
import functools

#### decorator to lof SQL queries

def log_queries(func):
    def wrapper(*args, **kwargs):
        print(f"args: {args}")
        # print(f"kwargs: {kwargs}")
        for k,v in kwargs.items():
            print(f"{k}: {v}")
        # return result
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
