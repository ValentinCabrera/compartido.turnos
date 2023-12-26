from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from .managers import UserManager
from django.utils import timezone
from django.utils.crypto import get_random_string

from back.utils import async_email
class User(models.Model):
    GRUPOS = [
        [1, 'cliente'],
        [2, 'profesional'],
        [3, 'administrador']
    ]

    mail = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    mail_is_checked = models.BooleanField(default=False)
    grupo = models.SmallIntegerField( choices=GRUPOS, default=1)

    objects = UserManager()

    def __str__(self):
        return self.name + " " + self.surname

    def hash_password(self):
        self.password = make_password(self.password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def get_auth_token(self):
        try:
            token = self.token

        except:
            token = Token.objects.create(user=self)

        return token.key

    def check_mail(self, key):
        token = self.get_auth_token()

        if token == key:
            self.mail_is_checked = True
            self.save()

            self.token.delete()
            return True

        return False
    def send_check_mail(self):
        token = self.get_auth_token()
        subject = "Verificacion de mail."
        context = {"token": token, "url": f"http://localhost:3000/checklogin/{token}", "name": self.name}
        recipient_list = [self.mail]
        async_email(subject=subject, recipient_list=recipient_list, context=context)

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = get_random_string(length=50)
        return super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(days=7)