from datetime import datetime

from application import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(150))
    email = db.Column(db.String(50))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    salt = db.Column(db.String(100))
    created_at = db.Column(db.Text)

    def __init__(self, name=None, password=None, email=None, role_id=None, salt=None):
        self.name = name
        self.password = password
        self.email = email
        self.role_id = role_id
        self.salt = salt
        self. created_at = datetime.utcnow()

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    User = db.relationship('User', backref=db.backref('roles', lazy=True))
