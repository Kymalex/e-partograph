# app/auth/views.py

# 3rd party imports
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

# local imports
from . import auth
from app.auth.forms import LoginForm, RegistrationForm
from app import db
from app.models import Nurse

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add a nurse to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        nurse = Nurse(emp_id=form.emp_id.data, firstname=form.firstname.data, lastname=form.lastname.data, password=form.password.data)

        # add nurse to the database 
        db.session.add(nurse)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log a nurse in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether nurse exists in the database and whether
        # the password entered matches the password in the database
        nurse = Nurse.query.filter_by(emp_id=form.emp_id.data).first()
        if nurse is not None and nurse.verify_password(
                form.password.data):
            # log nurse in
            login_user(nurse)

            # redirect to the dashboard page after login
            return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid employee id or password.')

    # load login template
    return render_template('login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log a nurse out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
