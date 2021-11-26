import os
import mysql.connector as DB


def open_database():
    try:
        user_name = os.environ.get('USER_NAME')
        password = os.environ.get('PASSWORD')
        host = os.environ.get('HOST')
        database = os.environ.get('DB_NAME')

        connection = DB.connect(user=os.environ.get('USER_NAME'),
                                password=os.environ.get('PASSWORD'),
                                host=os.environ.get('HOST'),
                                database=os.environ.get('DB_NAME'))
    except DB.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        cursor = connection.cursor(cursor_factory=DB.Cursor)
        ret_value = function(cursor, *args, **kwargs)
        cursor.close()
        connection.close()
        return ret_value

    return wrapper
