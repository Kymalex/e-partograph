# app/__init__.py

# inbuilt imports
from datetime import datetime

# third party plugins
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# local imports
from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "You must be logged in to access this page."

    migrate = Migrate(app=app, db=db)

    # import database models
    from app.models import Nurse, Patient, Ward, Record

    Bootstrap(app)
    
    # register blueprints
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    from app.patient import patient as patient_blueprint
    app.register_blueprint(patient_blueprint)
    from app.ward import ward as ward_blueprint
    app.register_blueprint(ward_blueprint)
    return app
