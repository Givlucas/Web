from flask import Flask



app = Flask(__name__)

# blueprint for auth routes in our app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from routes import routes as routes_blueprint
app.register_blueprint(routes_blueprint)
