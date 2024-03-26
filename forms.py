from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, TextAreaField 
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo = StringField("Photo URL", validators=[Optional(), URL()])
    age = FloatField("Age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    

class EditPetForm(FlaskForm):
    photo = StringField("Photo URL", validators=[Optional(), URL()])
    age = FloatField("Age", validators=[Optional()])
    available = BooleanField("Available?")
    species = StringField("Species", validators=[InputRequired()])
    notes = TextAreaField("Notes", validators=[Optional()])