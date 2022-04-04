from fapp import db
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    organization = db.Column(db.String(100))
    registered_on = db.Column(db.DateTime)
    confirmed_on = db.Column(db.DateTime)
    confirmed = db.Column(db.Boolean, default = False)
