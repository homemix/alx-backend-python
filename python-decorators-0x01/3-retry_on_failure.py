import functools
import sqlite3
import time


#### paste your with_db_decorator here
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


def retry_on_failure(retries=3, delay=2):
    """
    Retry on failure.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed with error: {e}")
                    if attempts == retries:
                        print("All retry attempts failed.")
                        raise
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
            return None

        return wrapper

    return decorator


""" your code goes here"""


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
