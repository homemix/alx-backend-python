import mysql.connector


def connect_to_db():
    """Connect to the MySQL database."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="<PASSWORD>",
            database="ALX_prodev"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def stream_user_ages():
    """
    A generator that yields user ages one by one from the database.
    """
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        # Yield ages one by one
        for age in cursor.fetchall():
            yield age[0]

        cursor.close()
        connection.close()


def calculate_average_age():
    """
    Calculates the average age of users using a generator.
    """
    total_age = 0
    count = 0

    # Use the generator to stream user ages
    for age in stream_user_ages():
        total_age += age
        count += 1

    # Calculate the average age
    if count > 0:
        average_age = total_age / count
        return average_age
    else:
        return 0
