import os

from flask import Flask, render_template

app = Flask(__name__)

FULL_NAME = {
    "first": os.environ.get("first_name"),
    "last": os.environ.get("last_name")
}

@app.route("/cover_letter", methods=["POST", "GET"])
def show_cover_letter():

    return render_template("cover_letter.html", name=FULL_NAME)


@app.route("/")
def homepage():

    return render_template("home.html", name=FULL_NAME)
