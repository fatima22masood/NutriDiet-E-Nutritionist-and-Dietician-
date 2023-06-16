from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, IntegerField, RadioField,FloatField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp
class UserInfoForm(FlaskForm):

    name = StringField('Name:', validators=[
    DataRequired(message="No valid value"),
    Length(min=2, max=20, message="Name must be between 2 and 20 characters"),
    Regexp('^[A-Za-z\s]+$', message="Name can only contain letters and spaces")])
    weight = IntegerField('Weight (Kg):', validators=[
    DataRequired(message="No valid value"),
    NumberRange(min=20, max=600, message="Weight must be between 20kg and 600kg")])
    height = FloatField('Height (cm):', validators=[DataRequired(message="No valid value"), NumberRange(min=60, max=220, message="Height must be between 60cm and 220cm")] )
    age = IntegerField('Age:', validators=[DataRequired(message="No valid value"), NumberRange(min=10, max=100, message="Age must be between 10 and 100 years")])
    gender = RadioField('Gender',choices=[('Male','Male'),('Female','Female')],default='Male',validators=[DataRequired()])
    physical_activity=RadioField('Physical Activity',
	    						choices=[
	    									('value1','Sedentary(little or no exercise)'),
	    									('value2','Light Active(1-3 days/week)'),
	    									('value3','Moderately Active(3-5 days/week)'),
	    									('value4','Very Active(6-7 days/week)'),
	    									('value5','Super Active(twice/day)')

	    								],
	    						default='value1',
	    						validators=[DataRequired()])
    submit = SubmitField('Generate Diet Plan')