import os

# import mysql.connector as DB
import pymysql

# import MySQLdb


def open_database():

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

    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        ret_value = function(cursor, *args, **kwargs)
        connection.commit()
        connection.close()
        return ret_value

    return wrapper
