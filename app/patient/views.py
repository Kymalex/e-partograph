# app/patient/views.py

# 3rd party imports
from flask import render_template, flash
from flask_login import current_user

# local imports
from . import patient
from app.patient.forms import CreatePatient
from app.models import Patient

@patient.route('/patient', methods=['GET', 'POST'])
def create():
  '''
  create a new patient
  '''

  form = CreatePatient()
  if form.validate_on_submit():
    if Patient.query.filter_by(email=form.email.data).first() is None:
      new_patient = Patient(firstname=form.firstname.data, lastname=form.lastname.data, age=form.age.data, phone_no=form.phone_no.data, email=form.email.data, id_no=form.id_no.data, nhif_no=form.nhif_no.data, ward_id=form.ward.data)
      new_patient.save()
      flash('Successfully created a new patient')
    flash('Error, patient already exists')

  return render_template('patient/create.html', title="Patient", form=form)

@patient.route('/patient/<int:id>', methods=['GET', 'POST'])
def fetch_records():
  '''
  fetch a patients records
  '''
