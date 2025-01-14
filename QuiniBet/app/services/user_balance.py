from app.services.command import TareaCommand


class UserBalance(TareaCommand):
    
    def __init__(self):
        pass

    def execute(self, model):
        self.send_bill(model)
        return
    
    def send_bill(self, model):
        print(f'Envío facturación de {model.name} suscripción VIP')