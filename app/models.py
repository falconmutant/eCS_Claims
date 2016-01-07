from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ecsclaims.encryption import AESCipher
from .utils import secret_key_gen

class App(models.Model):
    app = models.CharField(max_length=50, default='App')
    credenciales = models.OneToOneField(User, related_name='+')
    secret_key = models.CharField(max_length=64)
    admins = models.ManyToManyField(User)

    def __str__(self):
        return "%s" % self.app

    def get_key(self):
        return AESCipher(settings.CIPHER_KEY).decrypt(self.secret_key)

    def set_key(self, key):
        self.secret_key = AESCipher(settings.CIPHER_KEY).encrypt(key)
        creds = self.credenciales
        creds.set_password(key)
        creds.save()
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            key = secret_key_gen()
            self.secret_key = AESCipher(settings.CIPHER_KEY).encrypt(key)
            creds = self.credenciales
            creds.set_password(key)
            creds.is_staff = True
            creds.save()
        super(App, self).save(*args, **kwargs)
