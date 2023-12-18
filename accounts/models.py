from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from .managers import UserManager
from django.utils import timezone
from django.utils.crypto import get_random_string
class User(models.Model):
    mail = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    is_checked = models.BooleanField(default=False)

    objects = UserManager()

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

    def send_mail(self):
        pass

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