from app.models.card import Card
from app import db
from app.repositories import CardRepository


class CardService:
    def __init__(self):
        self.__repository = CardRepository()
    
    def find_by_id(self, card_id) -> Card:
        return Card.query.get(card_id)
    
    def find_by_numbers(self, numbers) -> Card:
        return self.__repository.find_by_numbers(numbers)

    def create_card(self, numbers, user_id) -> Card:
        new_card = Card(numbers=numbers, user_id=user_id)
        db.session.add(new_card)
        db.session.commit()
        return new_card

    def delete(self, card_id):
        return self.__repository.delete(card_id) 
