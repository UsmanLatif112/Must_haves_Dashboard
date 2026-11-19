import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_cors import CORS
app = Flask(__name__)
from dotenv import load_dotenv

CORS(app)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/"



from views import *
load_dotenv('.env')
SESSION_COOKIE_DOMAIN = os.getenv('SESSION_COOKIE_DOMAIN')
SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE')
SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SAMESITE')
FLASK_HOST = os.getenv('FLASK_HOST')
FLASK_PORT = os.getenv('FLASK_PORT')
FLASK_DEBUG = os.getenv('FLASK_DEBUG')
BS_TRAFFIC_URL = os.getenv("BS_TRAFFIC_URL")

print(f"SESSION_COOKIE_DOMAIN: {SESSION_COOKIE_DOMAIN}")
print(f"SESSION_COOKIE_SECURE: {SESSION_COOKIE_SECURE}")
print(f"SESSION_COOKIE_SAMESITE: {SESSION_COOKIE_SAMESITE}")
print(f"FLASK_HOST: {FLASK_HOST}")
print(f"FLASK_PORT: {FLASK_PORT}")
print(f"FLASK_DEBUG: {FLASK_DEBUG}")

print(f"BS_TRAFFIC_URL: {BS_TRAFFIC_URL}")


cookie_domain = os.getenv('SESSION_COOKIE_DOMAIN')
if cookie_domain:
    app.config['SESSION_COOKIE_DOMAIN'] = cookie_domain

app.config['SESSION_COOKIE_SECURE'] = os.getenv('SESSION_COOKIE_SECURE') == 'True'
app.config['SESSION_COOKIE_SAMESITE'] = os.getenv('SESSION_COOKIE_SAMESITE')


if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=int(FLASK_PORT), debug=FLASK_DEBUG=='True')

    
# from views import *
# app.config['SESSION_COOKIE_DOMAIN'] = '164.68.114.111'

# app.config['SESSION_COOKIE_SECURE'] = False
# app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'


# if __name__ == "__main__":
#     app.run(host='164.68.114.111', port=5005, debug=False)

