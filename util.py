def check_user_password(username, password, user):
    return (
        True if user["username"] == username and user["password"] == password else False
    )
