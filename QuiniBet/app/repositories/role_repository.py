from app import db
from app.models import Role



class RoleRepository():

    def create(self, role: Role):
        db.session.add(role)
        db.session.commit()
        return role
