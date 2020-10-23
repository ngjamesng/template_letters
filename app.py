from get_bulletpoints import get_bulletpoints
from flask import Flask, render_template
from forms import AddTextForm
from defaults import FULL_NAME, DEFAULT, SECRET_KEY

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY

@app.route("/cover_letter", methods=["POST", "GET"])
def show_cover_letter():

    form = AddTextForm(data=DEFAULT)

    if form.validate_on_submit():
        greeting = form.greeting.data
        intro = form.intro.data
        interest_reason = form.interest_reason.data
        outro = form.outro.data
        company_name = form.company_name.data
        bulletpoints = get_bulletpoints("text_files/bulletpoints.txt")
        return render_template("cover_letter_display.html",
                               greeting=greeting,
                               name=FULL_NAME,
                               intro=intro,
                               interest_reason=interest_reason,
                               company_name=company_name,
                               bulletpoints=bulletpoints,
                               outro=outro
                               )
    else:
        return render_template("cover_letter_form.html", form=form, default=DEFAULT)


@app.route("/")
def homepage():

    return render_template("home.html", name=FULL_NAME)
