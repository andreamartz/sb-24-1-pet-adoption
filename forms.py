from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf, URL, Length


class PetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[
                       InputRequired(message="Name cannot be blank.")])
    species = SelectField("Species Name", choices=[
        ('cat', 'cat'), ('dog', 'dog'), ('por', 'porcupine')],
        validators=[
        InputRequired(message="Species cannot be blank."),
        AnyOf(['cat', 'dog', 'porcupine'], message="Species must be cat, dog, or porcupine.")])
    photo_url = StringField("Photo URL", validators=[
                            Optional(),
                            URL(require_tld=True, message="URL must be valid.")])
    age = IntegerField("Age", validators=[
        Optional(),
        NumberRange(min=0, max=30, message="Age must be a whole number between 0 and 30.")])
    notes = StringField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available")
