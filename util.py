def check_user_password(username, password, user):
    print(user)
    return (
        True if user[0]["username"] == username and user[0]["password"] == password else False
    )
