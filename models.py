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

    image = db.Column(db.String, nullable=False, default=default_image_url)

    def serialize_cupcake(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image}

class AddCupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    flavor = StringField("Cupcake Flavor")
    size  = StringField('Size')
    rating = FloatField("Rating")
    image = URLField("URL to image",
                        validators=[URL(), Optional()])
