from app import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60))
    lastname = db.Column(db.String(20))
    user = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(500))

    def __init__(self, firstname, lastname, user, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.user = user
        self.email = email
        self.password = password

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self


class Data(db.Model):

    __tablename__ = 'Data'

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(12), unique=True)
    status = db.Column(db.String(7))
    error_code = db.Column(db.Integer)

    def __init__(self, version, status, error_code):
        self.version = version
        self.status = status
        self.error_code = error_code
    
    def save(self):
        db.session.add(self)
        db.session.commit()

        return self