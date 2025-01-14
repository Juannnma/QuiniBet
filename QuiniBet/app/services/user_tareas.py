from app.services import UserService, EmailService, UserBalance, RewardPoint, Tarea

class UserTarea:
    def __init__(self):
        self.__tarea = Tarea()
        self.__tarea.add_tarea(UserService())
        self.__tarea.add_tarea(EmailService())
        self.__tarea.add_tarea(UserBalance())
        self.__tarea.add_tarea(RewardPoint())
    
    
    def register(self, user):
        self.__tarea.execute(user)