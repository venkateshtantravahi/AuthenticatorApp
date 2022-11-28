import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Get the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('app.config.Config')

db = SQLAlchemy(app)
bc = Bcrypt(app)

lm = LoginManager()
lm.init_app(app)


# database setup
@app.before_first_request
def initialize_database():
    db.create_all()
    


# Importing views and models from app
from app import views, models
