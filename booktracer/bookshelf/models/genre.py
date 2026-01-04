from django.db import models




class Genre(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
