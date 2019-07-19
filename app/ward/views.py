# app/ward/views.py

# 3rd party imports
from flask import render_template, flash, redirect, url_for

# local imports
from . import ward
from app.models import Ward
from app.ward.forms import CreateWard

@ward.route('/ward', methods=['GET', 'POST'])
def create():
  '''
  create a new ward
  '''
  
  form = CreateWard()
  if form.validate_on_submit:
    ward = Ward.query.filter_by(name=form.name.data).first()
    if ward is None:
      ward = Ward(name=form.name.data)
      ward.save()
      flash('Successfully created a new ward')
      return redirect(url_for('home.dashboard'))
    else:
      flash('Ward already exists')
      return redirect(url_for('ward.create'))
  else:
    return redirect(url_for('ward.create'))

  return render_template('ward/create.html', form=form)
