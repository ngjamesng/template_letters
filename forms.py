from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class AddTextForm(FlaskForm):
    """Form for adding text."""

    greeting = StringField("Hello:")
    intro = TextAreaField("Intro Paragraph:")
    outro = TextAreaField("Outro paragraph:")