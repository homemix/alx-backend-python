import mysql.connector


def connect_to_db():
    """
    Connects to the MySQL database
    """
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



def stream_users_in_batches(size):
    """
    Get data in batches
    """
    connection = connect_to_db()
    if connection:

        cursor = connection.cursor()
        offset = 0
        while offset < size:
            cursor.execute("SELECT * FROM users LIMIT {size}")
            rows = cursor.fetchall()
            for row in rows:
                yield row
            offset += size
        cursor.close()
        connection.close()
    else:
        print("Connection closed/error")


def batch_processing(batch_size):
    """
    Processes batches to filter users with age > 25.
    """
    for batch in stream_users_in_batches(batch_size):
        filtered = [user for user in batch if user['age'] > 25]
        # yield filtered
        for user in filtered:
            print(user)
