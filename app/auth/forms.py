# app/auth/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo

# local imports
from app.models import Nurse


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    emp_id = StringField('Employee ID', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_emp_id(self, field):
        if Nurse.query.filter_by(emp_id=field.data).first():
            raise ValidationError('employee ID is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    emp_id = StringField('Employee ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
