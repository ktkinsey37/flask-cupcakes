"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import Length, URL, Optional, NumberRange

default_image_url = "https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg"

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    def __repr__(self):
        c = self
        return f'<Cupcake {c.id} {c.flavor} {c.size} {c.rating}>'

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    flavor = db.Column(db.String(50),
                    nullable=False)

    size = db.Column(db.String(50), nullable=False)

    rating = db.Column(db.Float, nullable=False)

    photo_url = db.Column(db.String, nullable=False, default=default_image_url)



class AddCupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    name = StringField("Pet Name")
    species = SelectField('Species',
  choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine', 'Porcupine')]
)
    photo_url = URLField("URL to Pet's Picture",
                        validators=[URL(), Optional()])
    age = IntegerField("Pet's Age in Years",
                        validators=[NumberRange(0,30)])
    notes = StringField("Any Addition Notes for Pet")

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = URLField("URL to Pet's Picture",
                        validators=[URL(), Optional()])
    notes = StringField("Any Additional Notes for Pet")
    available = BooleanField("Is this pet still available for adoption?")