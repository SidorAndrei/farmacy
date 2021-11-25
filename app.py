from flask import Flask, render_template, url_for, redirect
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)