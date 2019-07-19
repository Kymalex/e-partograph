# app/patient/__init__.py

# 3rd party imports
from flask import Blueprint

patient = Blueprint('patient', __name__)

# local imports
from . import views
