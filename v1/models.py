from app import db
from flask_login import UserMixin

from sqlalchemy import Column, Integer, String, Float


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    is_active = db.Column(db.Boolean)
    password = db.Column(db.String(255), nullable=False)  # Plain text password


class ApiResponse(db.Model):
    __tablename__ = "api_response"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to users table
    user = db.relationship('User', backref=db.backref('api_responses', lazy=True))
    description = Column(String(256))
    api = Column(String(512))
    method = Column(String(128))
    response_code = Column(Integer)
    result_according_to_response = Column(String(256))
    response_time = Column(Float)
    response_message = Column(String(1024))
    response_data = Column(db.Text)
    response_data_result = Column(String(256))
