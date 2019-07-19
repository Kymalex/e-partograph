# app/home/views.py

# 3rd party imports
from flask import render_template
from flask_login import login_required

# local import
from . import home

@home.route('/')
def index():
  return render_template('index.html', title="E-partograph")

@home.route('/dashboard')
@login_required
def dashboard():
  return render_template('dashboard.html', title='dashboard')
