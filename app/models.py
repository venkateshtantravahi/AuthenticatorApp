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
