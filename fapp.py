from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
db = SQLAlchemy()

app = Flask(__name__)
mail = Mail()

app.config['SECRET_KEY'] = 'adfg3653u65$^W#^W$TG$TV4vttV$TVrg%&&n8nV$5V#V#@%Vbvtyhyh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lucas:#390083816LLll@db.internal.io/webtest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURITY_PASSWORD_SALT'] = "ASD8&&s*$#6ksdf8*^&&SDF&^SD"

#mail
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'tt6564110@gmail.com'
MAIL_PASSWORD = '@390083816LLll'
MAIL_DEFAULT_SENDER = 'tt6564110@gmail.com'


def create_app():

    db.init_app(app)
    mail.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    login_manager.login_message_category = 'warning'
    from models import Users as User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
