from app import db
from app.repositories import RaffleRepository
from sqlalchemy.orm.exc import NoResultFound


class RaffleService:
    def __init__(self):
        self.__repository = RaffleRepository()

    def create(self, entity):
        return self.__repository.create(entity)
    

    def find_all(self):
        try:
            raffle = self.__repository.find_all()
            if raffle:
                return raffle
            else:
                return []
            
        except Exception as e:
            raise Exception('Error al obtener la lista de Sorteos' + str(e))


    def find_by_id(self, entity_id):
        try:
            entity = self.__repository.find_by_id(entity_id)
            if entity:
                return entity
            else:
                return None 
        except NoResultFound:
            return None
        except Exception as e:
            raise Exception('Error al obtener Sorteo por id: ' + str(e))
        

    def update(self, raffle_id, updated_fields):
        try:
            raffle = self.__repository.find_by_id(raffle_id)

            if raffle:
                for field, value in updated_fields.items():
                    setattr(raffle, field, value)

                db.session.commit()

            return raffle
        except Exception as e:
            raise Exception('Error al actualizar el Sorteo: ' + str(e))
        

    def delete(self, entity_id):
        return self.__repository.delete(entity_id) 