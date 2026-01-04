from django.db import models


class Authors(models.Model):
    nickname = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.DateField()
    death_date = models.DateField()
    description = models.TextField()
    sex = models.CharField(max_length=1)
    country = models.CharField(max_length=256)