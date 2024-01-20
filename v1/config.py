from datetime import timedelta


class Config:
    SECRET_KEY = "0332033603250309"  # You should set a secret key here
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:DSJoker%40%40112@localhost:3306/agency_apidb"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
