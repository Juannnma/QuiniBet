from app.services.command import TareaCommand


class RewardPoint(TareaCommand):
    def __init__(self):
        pass

    def reward_point(self, model, point):
        print(f' {model.name} te regalamos {point} creditos')
    #Asignar los creditos
    

    def execute(self, model):
        self.reward_point(model, '10')
        return

    #Buscar como validar el pais por la IP

    