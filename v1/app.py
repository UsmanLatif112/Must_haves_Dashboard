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
app.config['SESSION_COOKIE_DOMAIN'] = '127.0.0.1'

app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)



    
    
    
# from views import *
# app.config['SESSION_COOKIE_DOMAIN'] = '164.68.114.111'

# app.config['SESSION_COOKIE_SECURE'] = False
# app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'


# if __name__ == "__main__":
#     app.run(host='164.68.114.111', port=5005, debug=False)

    


