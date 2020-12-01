from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    pet_name=StringField('Pet Name', validators=[InputRequired()])
    species=SelectField('Species', choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url=StringField('Photo URL', validators=[Optional(), URL()])
    age=IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes=StringField('Notes', validators=[Optional(), Length(min=10)])




class EditPetForm(FlaskForm):
    """Form for editing a pet"""

    photo_url=StringField('Photo URL', validators=[Optional(), URL()])
    notes=StringField('Notes', validators=[Optional(), Length(min=10)])
    available=BooleanField('Available')