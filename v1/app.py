from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)


app.config.from_object("config.Config")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/"

from views import *

if __name__ == "__main__":
    app.run(debug=True)
