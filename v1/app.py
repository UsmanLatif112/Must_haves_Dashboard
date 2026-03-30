import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import timedelta
from config import Config

app = Flask(__name__)

# Import config from same folder
app.config.from_object(Config)

CORS(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/"
from views import *


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)