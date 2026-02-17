from datetime import timedelta


# class Config:
#     SECRET_KEY = "0332033603250309"  # You should set a secret key here
#     SQLALCHEMY_DATABASE_URI = (
#         "mysql+pymysql://root:DSJ%4003360325@localhost:3306/agency_apidb"
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SESSION_COOKIE_SECURE = True
#     REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
        


class Config:
    SECRET_KEY = "0332033603250309"  # You should set a secret key here
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://Admin_User:Dashboard%40CB8@164.68.114.111:3306/agency_apidb"
        # "mysql+pymysql://root:Noman.123@localhost:3306/agency_apidb"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_DURATION = timedelta(seconds=20)


