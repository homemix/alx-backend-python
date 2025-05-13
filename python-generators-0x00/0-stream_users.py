def stream_users():
    """
    Generator to fetch users from db
    """
    import mysql

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="<PASSWORD>",
            database="database",
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()