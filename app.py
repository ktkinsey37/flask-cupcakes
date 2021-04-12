"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, AddPetForm, EditPetForm
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import Length, URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'password'  

connect_db(app)
db.create_all()


@app.route('/', methods=["GET"])
def homepage():
    pets = Pet.query.all()
    return render_template("pets.html", pets=pets)