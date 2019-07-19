#app/patient/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

# local imports
from app.models import Ward

class CreatePatient(FlaskForm):
  '''
  create a new patient
  '''

  firstname = StringField('First Name', validators=[DataRequired()])
  lastname = StringField('Last Name', validators=[DataRequired()])
  age = StringField('Age', validators=[DataRequired()])
  email = StringField('Email ', validators=[DataRequired()])
  phone_no = StringField('Phone No', validators=[DataRequired()])
  id_no = StringField('ID No')
  nhif_no = StringField('NHIF No')
  ward = QuerySelectField(query_factory=lambda: Ward.query.all(), get_label="name")
  add = SubmitField('Add Patient')

