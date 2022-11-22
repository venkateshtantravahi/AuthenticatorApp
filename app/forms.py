from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired


class LoginForm(FlaskForm):
    username = StringField(u'Username', validators=[DataRequired()])
    password = PasswordField(u'Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    firstname = StringField(u'FirstName', validators=[DataRequired()])
    lastname = StringField(u'LastName', validators=[DataRequired()])
    username = StringField(u'Username', validators=[DataRequired()])
    password = PasswordField(u'Username', validators=[DataRequired()])
    email = StringField(u'Email', validators=[DataRequired(), Email()])

