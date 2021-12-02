import os

# import mysql.connector as DB
import pymysql

# import MySQLdb


def open_database():
    # try:
    #     user_name = os.environ.get('USER_NAME')
    #     password = os.environ.get('PASSWORD')
    #     host = os.environ.get('HOST')
    #     database = os.environ.get('DB_NAME')
    #
    #     connection = DB.connect(user=os.environ.get('lory_proiect'),
    #                             password=os.environ.get('6wMtZXNDFz#2'),
    #                             host=os.environ.get('localhost'),
    #                             database=os.environ.get('lory_proiect'))
    # except DB.DatabaseError as exception:
    #     print('Database connection problem')
    #     raise exception
    # return connection

    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Maruska27#",
            db="farmacy",
        )
    except pymysql.DatabaseError as exception:
        print("Database connection problem")
        raise exception

    # try:
    #     connection = MySQLdb.connect(host="localhost",
    #                  port=3306,
    #                  user="root",
    #                  password="Maruska27#",
    #                  db="farmacy")
    # except MySQLdb.DatabaseError as exception:
    #     print('Database connection problem')
    #     raise exception

    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        ret_value = function(cursor, *args, **kwargs)
        connection.close()
        return ret_value

    return wrapper
