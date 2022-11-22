import os
from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    CSRF_ENABLED = True
    # set up a secretkey/passcode
    SECRET_KEY = config('SECRET_KEY', default='s4cret_123')

    # db URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
