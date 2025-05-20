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
        finally:
            conn.close()
            print(" Database connection closed.")

    return wrapper


"""your code goes here"""


def transactional(func):
    """
    Return transactional function for db connection
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print(f"Transaction committed.")
            return result
        except Exception as error:
            conn.rollback()
            print(f"Transaction rolled back due to error:{error}")
            raise

    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


#### Update user's email with automatic transaction handling

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
