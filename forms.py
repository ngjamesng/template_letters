from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class AddTextForm(FlaskForm):
    """Form for adding text."""

    greeting = StringField("Hello:", validators=[DataRequired()])
    intro = TextAreaField("Intro Paragraph:")
    interest_reason = TextAreaField("Why you're interested Paragraph:")
    company_name = StringField("Company Name:", validators=[DataRequired()])
    outro = TextAreaField("Outro paragraph:")