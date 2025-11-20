import hashlib

from django.db import models


def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdiges()


def user_avatar(instance, filename):
    return f"user_{instance.user.id}/{filename}"


class Users(models.Model):
    nickname = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=2256)
    phone_number = models.DecimalField(max_digits=9, decimal_places=0, unique=True)
    avatar = models.ImageField(upload_to=user_avatar)

    def set_password(self, raw):
        self.password = hash_password(raw)

    def check_password(self, raw):
        return self.password == hash_password(raw)
    def __str__(self):
        return self.nickname

