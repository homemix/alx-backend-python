import functools
import sqlite3


def with_db_connection(func):
    """ your code goes here"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users1.db")
        try:
            # Pass the connection to the decorated function
            result = func(conn, *args, **kwargs)
            return result
        except Exception as e:
            print(f"Error In DB Connection: {e}")
            return None
        finally:
            conn.close()
            print("Database connection closed.")

    return wrapper


query_cache = {}


def cache_query(func):
    """
    Cache query results to avoid repeating.
    """

    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("Returning cached result for query.")
            return query_cache[query]

        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        print("Query result cached.")
        return result

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

print(users)
print(users_again)
