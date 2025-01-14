from app import db
from app.models import Card
from .repository_base import Create, Read, Update, Delete

class CardRepository(Create, Read, Update, Delete):
        
    def __init__(self):
        self.__model = Card

    def create(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def find_all(self):
        try:
            cards = db.session.query(self.__model).all()
            return cards
        except Exception as e:
            raise Exception('Error al obtener la lista de Card'  + str(e))

    def find_by_numbers(self, numbers):
        try:
            entity = db.session.query(self.__model).filter(self.__model.numbers == numbers).first()
            return entity
        except Exception as e:
            raise Exception('Error al obtener card por numeros' + str(e))

    def find_by_id(self, id):
        try:
            entity = db.session.query(self.__model).filter(self.__model.id == id).one()
            return entity
        except Exception as e:
            raise Exception('Error al obtener card por id' + str(e))
    
    def update(self, entity: Card):
        db.session.merge(entity)
        db.session.commit()
        return entity

    def delete(self, card_id):
        card = db.session.query(self.__model).get(card_id)
        if card:
            db.session.delete(card)
            db.session.commit()
            return True
        return False

