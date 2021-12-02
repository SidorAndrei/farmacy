from flask import Flask, render_template, url_for, redirect, request
import requests
import database_manager
import dotenv

dotenv.load_dotenv()


app = Flask(__name__)


@app.route("/")
def main_page(message1="", message2=""):
    meds = database_manager.get_meds()
    return render_template(
        "index.html", meds=meds, message1=message1, message2=message2
    )


@app.route("/login", methods=["post"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user_credentials = database_manager.get_user_connection(username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
