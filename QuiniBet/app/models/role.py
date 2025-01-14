from app import db
from dataclasses import dataclass
from .relations import users_roles


@dataclass(init = False)
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column('id',db.Integer, primary_key=True,autoincrement=True)
    name = db.Column('name',db.String(250))
    description = db.Column('description',db.String(250))
    
    users = db.relationship('User', secondary=users_roles, back_populates='roles')