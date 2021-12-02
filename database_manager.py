import database_connection


@database_connection.connection_handler
def register_user(cursor, username, password):
    query = f"""
            INSERT INTO  users(username, password) 
            values ('{username}', '{password}')
                """
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
                WHERE username = {username};"""
    cursor.execute(query)
    return cursor.fetch()
