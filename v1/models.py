from app import db
from flask_login import UserMixin

from sqlalchemy import Column, Integer, String, Float, DateTime,Text

from sqlalchemy.sql import func

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    is_active = db.Column(db.Boolean)
    password = db.Column(db.String(255), nullable=False)  # Plain text password
    

class QuickAnalysisModel(UserMixin, db.Model):
    __tablename__ = "quick_analysis"

    id = db.Column(db.Integer, primary_key=True)
    test_case = db.Column(db.String(500), nullable=False)
    use_case = db.Column(db.String(500), nullable=False)
    result = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class ClientmoduleModel(UserMixin, db.Model):
    __tablename__ = "client_module"

    id = db.Column(db.Integer, primary_key=True)
    test_case = db.Column(db.String(500), nullable=False)
    use_case = db.Column(db.String(500), nullable=False)
    result = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    
class team_usermoduleModel(UserMixin, db.Model):
    __tablename__ = "user_team_module"

    id = db.Column(db.Integer, primary_key=True)
    test_case = db.Column(db.String(500), nullable=False)
    use_case = db.Column(db.String(500), nullable=False)
    result = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
class ce_traffic_Model(UserMixin, db.Model):
    __tablename__ = "ce_traffic_module"

    id = db.Column(db.Integer, primary_key=True)
    test_case = db.Column(db.String(500), nullable=False)
    use_case = db.Column(db.String(500), nullable=False)
    result = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
class tiger_traffic_Model(UserMixin, db.Model):
    __tablename__ = "tiger_traffic_module"

    id = db.Column(db.Integer, primary_key=True)
    test_case = db.Column(db.String(500), nullable=False)
    use_case = db.Column(db.String(500), nullable=False)
    result = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
class torrential_traffic_Model(UserMixin, db.Model):
    __tablename__ = "torrential_traffic_module"

    id = db.Column(db.Integer, primary_key=True)
    test_case = db.Column(db.String(500), nullable=False)
    use_case = db.Column(db.String(500), nullable=False)
    result = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    
    
    

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
    payload_data = db.Column(db.String(255), nullable=True)
    response_data_result = Column(String(256))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class umbrellaResponse(db.Model):
    __tablename__ = "umbrella_agency"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to users table
    user = db.relationship('User', backref=db.backref('umbrella_agency', lazy=True))
    description = Column(String(256))
    api = Column(String(512))
    method = Column(String(128))
    response_code = Column(Integer)
    result_according_to_response = Column(String(256))
    response_time = Column(Float)
    response_message = Column(String(1024))
    response_data = Column(db.Text)
    payload_data = db.Column(db.String(255), nullable=True)
    response_data_result = Column(String(256))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class stagingapiaResponse(db.Model):
    __tablename__ = "Agency_API_Staging"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to users table
    user = db.relationship('User', backref=db.backref('Agency_API_Staging', lazy=True))
    description = Column(String(256))
    api = Column(String(512))
    method = Column(String(128))
    response_code = Column(Integer)
    result_according_to_response = Column(String(256))
    response_time = Column(Float)
    response_message = Column(String(1024))
    response_data = Column(db.Text)
    payload_data = db.Column(db.String(255), nullable=True)
    response_data_result = Column(String(256))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
