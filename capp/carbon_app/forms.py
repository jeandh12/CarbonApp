from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired

class BusForm(FlaskForm):
    kms = FloatField('Enter the number of Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Enter the type of Fuel', validators=[InputRequired()],
                            choices=[('Diesel', 'Diesel'), ('Biodiesel', 'Biodiesel')])
    submit = SubmitField('Submit')

class CarForm(FlaskForm):
    kms = FloatField('Enter the number of Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Enter the type of Fuel', validators=[InputRequired()],
                            choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Biodiesel', 'Biodiesel'),
                                     ('Electric (Nordic)', 'Electric (Nordic)'), ('Electric (Europe)', 'Electric (Europe)')])
    submit = SubmitField('Submit')

class PlaneForm(FlaskForm):
    kms = FloatField('Enter the number of Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Enter the type of Fuel', validators=[InputRequired()],
                            choices=[('Scheduled flight (economy)', 'Scheduled flight (economy)'),
                                     ('Charter flight (economy)', 'Charter flight (economy)'),
                                     ('Scheduled flight (business)', 'Scheduled flight (business)')])
    submit = SubmitField('Submit')

class FerryForm(FlaskForm):
    kms = FloatField('Enter the number of Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Enter the type of Fuel', validators=[InputRequired()],
                            choices=[('Diesel', 'Diesel')])
    submit = SubmitField('Submit')

class MotorbikeForm(FlaskForm):
    kms = FloatField('Enter the number of Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Enter the type of Fuel', validators=[InputRequired()],
                            choices=[('Petrol', 'Petrol')])
    submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
    kms = FloatField('Enter the number of Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Enter the type of Fuel', validators=[InputRequired()],
                            choices=[('Non-electric', 'Non-electric'), ('Electric', 'Electric')])
    submit = SubmitField('Submit')

class WalkForm(FlaskForm):
    kms = FloatField('Enter the number of Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Enter the type of Fuel', validators=[InputRequired()],
                            choices=[('No Fossil Fuel', 'No Fossil Fuel')])  # Redundant field for walking but needed for form consistency
    submit = SubmitField('Submit')

class TrainForm(FlaskForm):
    kms = FloatField('Enter the number of Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Enter the type of Train', validators=[InputRequired()], 
                            choices=[('Diesel', 'Diesel'), ('Electric (Nordic)', 'Electric (Nordic)'), ('Electric (Europe)', 'Electric (Europe)')])
    submit = SubmitField('Submit')
