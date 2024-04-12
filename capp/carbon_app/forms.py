from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

class BusForm(FlaskForm):
  kms = FloatField('Enter the number of Kilometers', [InputRequired()])
  fuel_type = SelectField('Enter the type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Petrol', 'Petrol'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Enter the number of Kilometers', [InputRequired()])
  fuel_type = SelectField('Enter the type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Enter the number of Kilometers', [InputRequired()])
  fuel_type = SelectField('Enter the type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol')])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Enter the number of Kilometers', [InputRequired()])
  fuel_type = SelectField('Enter the type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Enter the number of Kilometers', [InputRequired()])
  fuel_type = SelectField('Enter the type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
  kms = FloatField('Enter the number of Kilometers', [InputRequired()])
  fuel_type = SelectField('Enter the type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
  kms = FloatField('Enter the number of Kilometers', [InputRequired()])
  fuel_type = SelectField('Enter the type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  
