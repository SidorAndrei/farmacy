from flask import Flask, render_template, url_for, redirect, request
import database_manager
import dotenv

import util

dotenv.load_dotenv()


app = Flask(__name__)


@app.route("/")
def main_page(message=""):
    meds = database_manager.get_meds()
    return render_template(
        "index.html", meds=meds, message=message
    )


@app.route("/login", methods=["post"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if len(username)>0:
        user_credentials = database_manager.get_user_connection(username)
        if util.check_user_password(username, password, user_credentials):
            return redirect(
                url_for('menu_page')
            )
        else:
            return redirect(
                url_for('main_page',
                        message="Incorrect password!")
            )
    else:
        return redirect(
            url_for('main_page',
                    message=('' if len(username) > 0 else "Please insert username!")
                    )
        )


@app.route("/menu")
def menu_page():
    return render_template("menu_page.html")


@app.route("/register")
def register_page(message=''):
    return render_template("register_page.html", message=message)


@app.route("/register-user", methods=['post'])
def register():
    if request.form.get("password") == request.form.get("confirmpassword"):
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        database_manager.register_user(username, password, email)
        return redirect(url_for('main_page'))
    else:
        return redirect(url_for('register_page', message="Passwords does not match!"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
