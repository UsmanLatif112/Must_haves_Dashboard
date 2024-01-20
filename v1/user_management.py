from flask_login import UserMixin
from app import login_manager, db
from models import User
from sqlalchemy import select

# User class for login management


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


def authenticate(email, password):
    user = User.query.filter_by(email=email, password=password).first()
    return user


def register(email, password):
    user = User(email=email, password=password)  # Store plain text password

    # Add to the session and commit
    db.session.add(user)
    db.session.commit()

    return user
