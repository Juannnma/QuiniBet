from app.repositories import UserRepository
from app import db
from sqlalchemy.orm.exc import NoResultFound

class UserService():
    def __init__(self):
        self.__repository = UserRepository()


    def create(self, entity):
        return self.__repository.create(entity)
    

    def find_all(self):
        try:
            users = self.__repository.find_all()
            if users:
                return users
            else:
                return []
            
        except Exception as e:
            raise Exception('Error al obtener la lista de usuarios' + str(e))

    
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
            raise Exception('Error al obtener usuario por id: ' + str(e))


    
    def update(self, entity_id, updated_fields):
        try:
            user = self.__repository.find_by_id(entity_id)

            if user:
                for field, value in updated_fields.items():
                    setattr(user, field, value)

                db.session.commit()

            return user
        except Exception as e:
            raise Exception('Error al actualizar el usuario: ' + str(e))
    
    def delete(self, entity_id):
        return self.__repository.delete(entity_id) 