
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from temariIfo import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(120),  nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}, {self.email}')"


class Images(db.Model):
    image_id = db.Column(db.Integer, primary_key = True)
    image_name = db.Column(db.String(50), unique=True, nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('universities.univ_id'), nullable=False)
    
    def __repr__(self):
        return f"Image('{self.image_name}')"

class Information(db.Model):
    info_id = db.Column(db.Integer, primary_key = True)
    institute_id = db.Column(db.Integer, db.ForeignKey('institutes.inst_id'), nullable=False)
    department = db.Column(db.String, unique=True, nullable=False)
    years = db.Column(db.Integer, nullable=False)
    objective= db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"Information('{self.department}')"


class Institutes(db.Model):
    inst_id = db.Column(db.Integer, primary_key = True)
    university_id = db.Column(db.Integer, db.ForeignKey('universities.univ_id'), nullable=False)
    institute_name = db.Column(db.String(150), nullable=False)
    phone_no = db.Column(db.String(50),  nullable=False)
    email= db.Column(db.String(50), nullable=False)
    description = db.Column(db.String, nullable=False)
    information = db.relationship('Information', backref='Institute', lazy=True)
    
    def __repr__(self):
        return f"Institute('{self.institute_name}')"

class Universities(db.Model):
    univ_id = db.Column(db.Integer, primary_key = True)
    univ_name = db.Column(db.String(150), unique=True, nullable=False)
    location = db.Column(db.String(150),  nullable=False)
    description = db.Column(db.String, nullable=False)
    institutes = db.relationship('Institutes', backref='University', lazy=True)
    image = db.relationship('Images', backref='University', lazy=True, uselist=False)
    
    def __repr__(self):
        return f"University('{self.univ_name}')"
