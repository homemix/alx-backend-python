import mysql.connector


def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="<Password>",
            database="ALX_prodev",
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None


def paginate_users(page_size, offset):

    """
    Fetch a single page of users from the database.
    """
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
        results = cursor.fetchall()
        cursor.close()
        return results
    return None


def lazy_paginate(page_size):
    """
    Generator that yields pages of user records lazily from the database.
    """
    connection = connect_to_db()
    if connection:
        offset = 0
        while True:
            page = paginate_users(connection, page_size, offset)
            if not page:
                break
            yield page
            offset += page_size
        connection.close()
