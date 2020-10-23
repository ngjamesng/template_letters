import os
from get_bulletpoints import get_bulletpoints
from flask import Flask, render_template
from forms import AddTextForm

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "secret key!!!!")


@app.route("/cover_letter", methods=["POST", "GET"])
def show_cover_letter():

    FULL_NAME = {
        "first": os.environ.get("first_name"),
        "last": os.environ.get("last_name")
    }

    DEFAULT = {
        "intro": "I'm James, a Software Engineer in San Francisco.",
        "outro": "I would be thrilled to hear back!"
    }

    form = AddTextForm(data=DEFAULT)

    if form.validate_on_submit():
        greeting = f"Hello {form.greeting.data},"
        intro = form.intro.data
        outro = form.outro.data
        bulletpoints = get_bulletpoints("text_files/bulletpoints.txt")
        return render_template("cover_letter_view.html", greeting=greeting, name=FULL_NAME, bulletpoints=bulletpoints)
    else:
        return render_template("cover_letter_form.html", form=form, default=DEFAULT)


@app.route("/")
def homepage():

    return render_template("home.html", name=FULL_NAME)
