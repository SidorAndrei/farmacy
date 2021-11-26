import database_connection


@database_connection.connection_handler
def get_meds(cursor):
    query = """
            SELECT Name
            FROM medicines
            ORDER BY Name"""
    cursor.execute(query)
    return cursor.fetchall()