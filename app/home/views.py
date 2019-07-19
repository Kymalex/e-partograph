# app/home/views.py

# 3rd party imports
from flask import render_template
from flask_login import login_required

# local import
from . import home
from app.models import Ward, Patient

@home.route('/')
def index():
  return render_template('index.html', title="E-partograph")

@home.route('/dashboard')
@login_required
def dashboard():
  patients = Patient.query.all()
  wards = Ward.query.order_by(Ward.id).all()
  return render_template('dashboard.html', title='dashboard', wards=wards, patients=patients)
