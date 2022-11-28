import os

from flask import render_template, request, url_for, redirect, send_from_directory
from flask_login import login_user, logout_user
from jinja2 import TemplateNotFound
import pandas as pd

from . import app, lm, bc
from app.forms import LoginForm, RegisterForm
from app.models import Users, Data


@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    msg = None
    success = False

    if request.method == 'GET':
        return render_template('register.html', form=form, msg=msg)

    if form.validate_on_submit():
        # assign data to variables
        firstname = request.form.get('firstname', '', type=str)
        lastname = request.form.get('lastname', '', type=str)
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        email = request.form.get('email', '', type=str)

        # filter user data for user_check
        user = Users.query.filter_by(user=username).first()

        user_by_email = Users.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: user already Exist!'

        else:
            pwd_hash = bc.generate_password_hash(password)

            user = Users(firstname, lastname, username, email, pwd_hash)
            user.save()

            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'
            success = True
    else:
        msg = 'Input Error'

    return render_template('register.html', form=form, msg=msg, success=success)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    msg = None

    if form.validate_on_submit():
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)

        user = Users.query.filter_by(user=username).first()

        if user:
            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = 'Wrong credentials, please check your passcode and try again'
        else:
            msg = 'unknown user!!'

    return render_template('login.html', form=form, msg=msg)


@app.route('/', defaults={'path': 'index'})
@app.route('/<path>')
def index(path):
    try:
        query = request.args.get('search')
        if query:
            results =  Data.query.filter(Data.status.contains(query) | Data.error_code.contains(query)).all()
            return render_template('index.html', results=results, query=query)

        else:
            return render_template('index.html', results=None, query=None)

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    except:
        return render_template('page-500.html'), 500


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')
