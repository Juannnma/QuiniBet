from app.services.command import TareaCommand


class EmailService(TareaCommand):
    
    def __init__(self):
        #TODO: COnfiguración de servidor de correo
        #self.smtp_server = smtplib.SMTP('mailhost', 25)
        pass

    def execute(self, model):
        self.sending_email(model.email, "Welcome to the jungle!")

    def sending_email(self, email, message):

        #TODO: Se envia un email e imprime un mensaje
        print(f'{message} and the mail {email}')

    