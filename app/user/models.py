from sqlalchemy.orm import relationship

from app.database import db
from app.event.models import Event


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        return f'<User {self.username}>'

class UserRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    confirm_password = db.Column(db.String(255), nullable=False)


    def __repr__(self):
        return f'<User {self.username}>'
