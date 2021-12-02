import database_connection


@database_connection.connection_handler
def register_user(cursor, username, password, email):
    query = f"""
            INSERT INTO farmacy.users(username, password, email) 
            VALUES 
            ('{username}', 
            '{password}', 
            '{email}');"""
    cursor.execute(query)




@database_connection.connection_handler
def get_meds(cursor):
    query = """
            SELECT *
            FROM medicines
            ORDER BY Name;"""
    cursor.execute(query)
    return cursor.fetchall()


@database_connection.connection_handler
def get_user_connection(cursor, username):
    query = f"""
                SELECT *
                FROM users
                WHERE username = '{username}';"""
    cursor.execute(query)
    return cursor.fetchall()
