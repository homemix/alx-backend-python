import functools
import sqlite3


def with_db_connection(func):
    """ your code goes here"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            # Pass the connection to the decorated function
            result = func(conn, *args, **kwargs)
            return result
        except Exception as e:
            print(f"Error In DB Connection: {e}")
            return None
        finally:
            conn.close()
            print(" Database connection closed.")

    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


#### Fetch user by ID with automatic connection handling

user = get_user_by_id(user_id=1)
print(user)
