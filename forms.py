from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired


class AdoptionForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    message = TextAreaField(validators=[DataRequired(), Length(max=400)])
    submit = SubmitField('Submit')


class CreateListingForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    pet_name = StringField(validators=[DataRequired()])
    animal = SelectField("dog", choices=[("dog", "dog"), ("cat", "cat"), ("others", "other animals")])
    breed = StringField(validators=[DataRequired()])
    dob = DateField('Pick a Date', format="%m/%d/%Y")
    description_of_pet = TextAreaField(validators=[Optional(), Length(max=200)])
    upload_img = FileField('image', validators=[
        FileRequired(),
        FileAllowed(tuple('jpg jpe jpeg png gif svg bmp webp'.split()), 'Images only!')
    ])
    submit = SubmitField('Submit')