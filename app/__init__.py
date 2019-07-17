# app/__init__.py

# inbuilt imports
from datetime import datetime

# third party plugins
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

db = SQLAlchemy()

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])


    db.init_app(app)

    migrate = Migrate(app=app, db=db)

    from app.models import Nurse, Patient, Ward, Record

    @app.route('/')
    def index():
        return render_template('home.html', title="Home", year=datetime.utcnow())

    
    return app