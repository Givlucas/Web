from flask import Blueprint
from flask import render_template
from flask_login import login_required, current_user
routes = Blueprint('routes', __name__)

@routes.route("/")
def index():
    return render_template('index.html')

@routes.route("/snapCode")
def snapCode():
    return render_template('snapCode.html')

@routes.route("/showroom")
def showroom():
    return render_template('general.html')

@routes.route("/goodbye")
def goodbye():
    return render_template('goodbye.html')

@routes.route("/profile")
@login_required
def profile():
    return render_template('profile.html', name=current_user.fname, lname=current_user.lname, email=current_user.email, organization=current_user.organization)
