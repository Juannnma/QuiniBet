from app.models import Role
from app.repositories import RoleRepository
from app import db

class RoleService():
    def __init__(self):
        self.__repositories = RoleRepository()

    def create(self, role: Role):
        self.__repositories.create(role)


    def update(self, role: Role):
        self.__repositories.update(role)
