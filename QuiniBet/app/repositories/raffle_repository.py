from app.models import Raffle
from .repository_base import Read, Create, Update, Delete
from app import db

class RaffleRepository(Create, Read, Update, Delete):
    def __init__(self):
        self.__model = Raffle

    def create(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def find_all(self):
            try:
                    raffles = db.session.query(self.__model).all()
                    return raffles
            except Exception as e:
                    raise Exception("Error al obtener la lista de raffles: " + str(e))

    
    def find_by_id(self, id):
            try:
                    entity = db.session.query(self.__model).filter(self.__model.id == id).one()
                    return entity
            except Exception as e:
                    raise Exception("Error al obtener usuario por ID: " + str(e))
    
    def find_by_name(self, name):
            try:
                    entity = db.session.query(self.__model).filter(self.__model.name == name).one()
                    return entity
            except Exception as e:
                    raise Exception("Error al obtener usuario por nombre de raffle: " + str(e))


    def update(self, entity: Raffle):
            db.session.merge(entity)
            db.session.commit()
            return entity


    def delete(self, id: int):
            entity = self.find_by_id(id)
            db.session.delete(entity)
            db.session.commit()
            return entity