from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class AdoptionForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    message = StringField(validators=[DataRequired(), Length(max=400)])
    submit = SubmitField('Submit')
