from django.db import models
class UserManager(models.Manager):
    def sign_in(self, mail, name, surname, password):
        user = self.create(mail=mail, name=name, surname=surname, password=password)
        user.hash_password()
        user.send_check_mail()

        return user

    def log_in(self, mail, password):
        try:
            user = self.get(mail=mail)

        except:
            raise Exception("Usuario o contraseña incorrectos.")

        if user.is_checked:
            if user.check_password(password):
                token = user.get_auth_token()
                return token

            else:
                raise Exception("Usuario o contraseña incorrectos.")

        else:
            user.send_mail()
            raise Exception("La cuenta no esta verificada.")