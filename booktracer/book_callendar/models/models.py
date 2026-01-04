from django.db import models

from booktracer.users.models import Users


class BookCalendary(models.Model):

    owner = models.ForeignKey(Users,
                                 on_delete=models.CASCADE)
    year = models.DecimalField(max_digits=1000, decimal_places=0)
    month = models.CharField(max_length=254)
    day = models.DecimalField
