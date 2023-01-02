from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class HelloForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), ])
    body = TextAreaField("Body", validators=[DataRequired(), ])
    submit = SubmitField("Submit")
