from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'adfg3653u65$^W#^W$TG$TV4vttV$TVrg%&&n8nV$5V#V#@%Vbvtyhyh'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lucas:@390083816LLll@db.internal.io/webtest'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
