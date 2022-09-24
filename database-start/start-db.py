# code to start initialize the database
# each part should only be run once
import os
from configparser import ConfigParser
from mysql.connector import connect, Error
"""
try:
    with connect(
        host="localhost",
        port=9999,
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = 'CREATE DATABASE pantry_tracker'
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)
"""
try:
    # get config file for database user and password
    config = ConfigParser()
    config.read(os.getenv('BACKEND_CONFIG'))
    username = config.get('pantry_db', 'user')
    passw = config.get('pantry_db', 'password')

    with connect(
        host="localhost",
        port=9999,
        user=username,
        password=passw,
        database="pantry_tracker",
    ) as connection:
        create_user_table_query = '''
        CREATE TABLE IF NOT EXISTS users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_name TEXT
        )
        '''
        create_pantry_items_table_query = '''
        CREATE TABLE IF NOT EXISTS pantry_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT
        )
        '''
        create_pantry_table_query = '''
        CREATE TABLE IF NOT EXISTS pantry (
            user_id INT,
            item_id INT,
            quantity INT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(item_id) REFERENCES pantry_items(id),
            PRIMARY KEY(user_id, item_id)
        )
        '''

        create_default_user_query = '''
        INSERT INTO users (user_name)
        VALUES ('default')
        '''

        with connection.cursor() as cursor:
            cursor.execute(create_user_table_query)
            cursor.execute(create_pantry_items_table_query)
            cursor.execute(create_pantry_table_query)
            cursor.execute(create_default_user_query)
            connection.commit()
except Error as e:
    print(e)