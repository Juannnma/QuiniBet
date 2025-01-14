from app import db
from datetime import datetime
from dataclasses import dataclass 

@dataclass
class Card(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    numbers = db.Column(db.String(255))
    date = db.Column(db.String(255))
    time = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='cards', lazy=True)

    def __init__(self, numbers, user_id):
        self.numbers = numbers
        self.user_id = user_id
        self.generate_date_and_time()

    def generate_date_and_time(self):
        current_datetime = datetime.utcnow()
        self.date = current_datetime.strftime('%Y-%m-%d')
        self.time = current_datetime.strftime('%H:%M:%S')
