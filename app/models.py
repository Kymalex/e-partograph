# app/models.py

# inbuilt import
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# local imports
from app import db, login_manager


class Nurse(UserMixin, db.Model):
    '''
    creates a nurses table
    '''

    __tablename__ = 'nurses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emp_id = db.Column(db.String(64), nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(255))
    is_admin  = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, emp_id, firstname, lastname, password):
        self.emp_id = emp_id
        self.firstname = firstname
        self.lastname = lastname
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Set up user_loader
    @login_manager.user_loader
    def load_user(user_id):
        return Nurse.query.get(int(user_id))

class Patient(db.Model):
    '''
    creates patients table
    '''

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_no = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64))
    id_no = db.Column(db.Integer)
    nhif_no = db.Column(db.String(64))
    ward_id = db.Column(db.Integer, db.ForeignKey('wards.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())


class Ward(db.Model):
    '''
    create wards table
    '''

    __tablename__ = 'wards'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    nurse_id = db.Column(db.Integer, db.ForeignKey('nurses.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())


class Record(db.Model):
    '''
    create records table
    '''
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
