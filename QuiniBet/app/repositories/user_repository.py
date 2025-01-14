from app import db
from app.models import User
from .repository_base import Create, Read, Update, Delete


    

class UserRepository(Create, Read, Update, Delete):
        
    def __init__(self):
            self.__model = User

    def create(self, model: User):
        db.session.add(model)
        db.session.commit()
        return model



    def find_all(self):
        try:
            users = db.session.query(self.__model).all()
            return users
        except Exception as e:
            raise Exception('Error a obtener la lista de usuarios'  + str(e))
    

    def find_by_id(self, id):
        try:
            entity = db.session.query(self.__model).filter(self.__model.id == id).one()
            return entity
        except Exception as e:
            raise Exception('Error a obtener usuario por id' + str(e))


    def update(self, entity: User):
            db.session.merge(entity)
            db.session.commit()
            return entity


    #Delete Section
    def delete(self, user_id) -> bool:
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    def register_user(self, user):
        print(user)
        self.create(user.username, user.email, user.password)

    def search(self, lease_min, lease_max):
        return db.session.query(self.__model).filter(self.__model.lease.between(lease_min, lease_max)).all()