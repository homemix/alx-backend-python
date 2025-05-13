import mysql.connector


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="<PASSWORD>",  # Replace with your MySQL root password
        database="ALX_prodev"
    )


def paginate_users(connection, page_size, offset):
    """
    Fetch a single page of users from the database.
    """
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    results = cursor.fetchall()
    cursor.close()
    return results


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
