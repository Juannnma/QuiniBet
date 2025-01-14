from app import db
from dataclasses import dataclass 
from .relations import users_roles, users_raffles

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250))
    surname = db.Column(db.String(250))
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(255))

    roles = db.relationship('Role', secondary=users_roles, back_populates='users')
    cards = db.relationship('Card', back_populates='user', lazy=True)
    raffles = db.relationship('Raffle', secondary=users_raffles, back_populates='participants')
