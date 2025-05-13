import mysql.connector
import csv
import uuid


DB_NAME = "ALX_prodev"

TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS user_data (
    user_id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age DECIMAL(5, 2) NOT NULL,
    INDEX(user_id)
);
"""

def connect_db():
    """
    Connect to MySQL database
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="<PASSWORD>",
        )
        return connection
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return None


def create_database(connection):
    """
    Create a database
    """
    cursor = connection.cursor()
    try:
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
        print(f'Database {DB_NAME} created')
    except mysql.connector.Error as err:
        print(f'Failed to create database {DB_NAME}: {err}')
    finally:
        cursor.close()

def connect_to_prodev():
    """
    Connect to a Prodev database
    """
    connection = connect_db()
    if connection is not None:
        create_database(connection)
        return connection
    else:
        return None

def create_tables(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(TABLE_SCHEMA)
        connection.commit()
    except mysql.connector.Error as err:
        print(f'Failed to create tables: {err}')
    finally:
        cursor.close()



def read_csv_generator(file_path):
    """
    Generator that reads user data from a CSV file.
    Yields each row as a tuple (user_id, name, email, age).
    """
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield (
                str(uuid.uuid4()),      # Generate a unique user_id
                row['name'],
                row['email'],
                float(row['age'])
            )


def insert_data(connection, data):
    """
    Insert data from a generator into the database.
    Avoid inserting duplicates (based on email).
    """
    cursor = connection.cursor()
    insert_query = """
                   INSERT INTO user_data (user_id, name, email, age)
                   VALUES (%s, %s, %s, %s) ON DUPLICATE KEY \
                   UPDATE name= \
                   VALUES (name), age= \
                   VALUES (age); \
                   """
    for record in data:
        try:
            cursor.execute(insert_query, record)
        except mysql.connector.Error as err:
            print(f"Failed to insert record {record}: {err}")

    connection.commit()
    cursor.close()
