from getpass import getpass
from mysql.connector import connect, Error

"""try:
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
    print(e)"""

"""try:
    with connect(
        host="localhost",
        port=9999,
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="pantry_tracker",
    ) as connection:
        create_user_table_query = '''
        CREATE TABLE users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_name TEXT
        )
        '''
        create_pantry_items_table_query = '''
        CREATE TABLE pantry_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT
        )
        '''
        create_pantry_table_query = '''
        CREATE TABLE pantry (
            user_id INT,
            item_id INT,
            quantity INT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(item_id) REFERENCES pantry_items(id),
            PRIMARY KEY(user_id, item_id)
        )
        '''
        with connection.cursor() as cursor:
            cursor.execute(create_user_table_query)
            cursor.execute(create_pantry_items_table_query)
            cursor.execute(create_pantry_table_query)
            connection.commit()
except Error as e:
    print(e)"""


try:
    with connect(
        host="localhost",
        port=9999,
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="pantry_tracker"
    ) as connection:
        show_table_query = "DESCRIBE pantry_items"
        with connection.cursor() as cursor:
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)