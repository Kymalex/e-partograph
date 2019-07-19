# app/ward/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

# local imports
from app.models import Nurse

class CreateWard(FlaskForm):
  name = StringField('Ward Name', validators=[DataRequired()])
  nurse = QuerySelectField(query_factory=lambda: Nurse.query.all(), get_label="name")
  add = SubmitField('Create Ward')
