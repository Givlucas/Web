from flask import Blueprint
from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import Users as User
from flask_login import login_user, login_required, logout_user, current_user
from fapp import db
import re

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():

    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.', 'warning')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('routes.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    confp = request.form.get('conf_password')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    org = request.form.get('organization')

    if  email == "" or password == "" or fname == "" or lname == "" or org == "":
        flash('One or more fields not completed', 'warning')
        return redirect(url_for('auth.signup'))

    if confp != password:
        flash('passwords do not match', 'warning')
        return redirect(url_for('auth.signup'))

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists. Go to login page', 'warning')
        return redirect(url_for('auth.signup'))

    if len(password) < 8:
        flash('Password too short', 'warning')
        return redirect(url_for('auth.signup'))

    if bool(re.search("[!@#$%^&]+", password)) != True:
        flash('Please include 1 or more special characters. ! @ # $ % ^ & ', 'warning')
        return redirect(url_for('auth.signup'))

    if bool(re.search("\d+", password)) != True:
        flash('Please include 1 or more digits.', 'warning')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, password=generate_password_hash(password, method='sha256'), fname=fname, lname=lname, organization=org)
    db.session.add(new_user)
    db.session.commit()
    flash('Account creation success!', 'success')
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@auth.route('/removed')
@login_required
def rm_user_account():
    usr_to_rm = User.query.filter_by(id=current_user.id).one()
    db.session.delete(usr_to_rm)
    db.session.commit()
    return redirect(url_for('routes.goodbye'))
