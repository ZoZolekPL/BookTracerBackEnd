from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    size = models.DecimalField(max_digits=200, decimal_places=0)
    description = models.TextField()

