from app import db
from dataclasses import dataclass
from .relations import users_raffles

@dataclass
class Raffle(db.Model):
    __tablename__ = 'raffles'
    id = db.Column('id',db.Integer, primary_key=True)
    card_win = db.Column('card_win',db.String(255))
    winners = db.Column('winners',db.String(255))
    date = db.Column('date',db.String(255))
    time = db.Column('time',db.String(255))
    prize = db.Column('prize',db.String(255))

    participants = db.relationship('User', secondary=users_raffles, back_populates='raffles')
