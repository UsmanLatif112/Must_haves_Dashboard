from datetime import timedelta
from lib import data



# class Config:
    # SECRET_KEY = "0332033603250309"  # You should set a secret key here
    # SQLALCHEMY_DATABASE_URI = (
    #     "mysql+pymysql://root:DSJ%4003360325@localhost:3306/agency_apidb"
    # )
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SESSION_COOKIE_SECURE = True
    # REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
    

class Config:
    SECRET_KEY = data.secret_key  # You should set a secret key here
    SQLALCHEMY_DATABASE_URI = data.sql_alchemy_database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
    

# class Config:
#     SECRET_KEY = "0332033603250309"  # You should set a secret key here
#     SQLALCHEMY_DATABASE_URI = (
#         "mysql+pymysql://root:root@localhost:3306/agency_apidb"
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SESSION_COOKIE_SECURE = True
#     REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
