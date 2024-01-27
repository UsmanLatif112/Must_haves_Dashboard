from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/"

from views import *
# app.config['SESSION_COOKIE_DOMAIN'] = '0.0.0.0'

# app.config['SESSION_COOKIE_SECURE'] = False
# app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

    # app.run(host='0.0.0.0', port=5005)

