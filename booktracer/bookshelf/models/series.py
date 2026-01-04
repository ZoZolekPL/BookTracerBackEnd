from django.db import models

from .authors import Authors


class BookSeries(models.Model):
    name = models.CharField(max_length=256)
    size = models.DecimalField(max_digits=30, decimal_places=0)
    author = models.ForeignKey(Authors,
                               on_delete=models.CASCADE)
    description = models.TextField()