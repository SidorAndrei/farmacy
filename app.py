from flask import Flask, render_template, url_for, redirect
import requests
import database_manager
import dotenv

dotenv.load_dotenv()


app = Flask(__name__)


@app.route("/")
def main_page():
    meds = database_manager.get_meds()
    return render_template(meds=meds)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        debug=True,
        port=5000)
