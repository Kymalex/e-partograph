# app/ward/__init__.py

# 3rd party imports
from flask import Blueprint

ward = Blueprint('ward', __name__)

# local imports
from . import views
