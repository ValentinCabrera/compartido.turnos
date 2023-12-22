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

        if user.mail_is_checked:
            if user.check_password(password):
                token = user.get_auth_token()
                return token, user.get_grupo_display()

            else:
                raise Exception("Usuario o contraseña incorrectos.")

        else:
            raise Exception("La cuenta no esta verificada.")

    def check_mail(self, token, mail, password):
        try:
            user = self.get(mail=mail)

        except:
            raise Exception("Usuario o contraseña incorrectos.")

        if not user.mail_is_checked:
            if user.check_password(password):
                if not user.check_mail(token):
                    raise Exception("Token de verificacion incorrecto.")

                else:
                     return user.get_auth_token()

            else:
                raise Exception("Usuario o contraseña incorrectos.")

        else:
            raise Exception("La cuenta ya ha sido verificada.")
