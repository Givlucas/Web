from flask import Blueprint
from flask import render_template

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
