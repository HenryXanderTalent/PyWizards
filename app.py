from flask import Flask, render_template, session
from flask_wtf import FlaskForm
from wtforms import (StringField, RadioField, 
                    SelectField, TextAreaField, SubmitField, IntegerField)
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)

# Get the categories from the API
categories = ['History', 'Food', 'Music']

class QuizForm(FlaskForm):
    category = SelectField(u'Select category', choices=categories)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = QuizForm()