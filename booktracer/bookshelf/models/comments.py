from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from booktracer.users.models import Users


class Comments(models.Model):
    author = models.ForeignKey(Users,
                               on_delete=models.CASCADE,
                               related_name="comment")
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
        ] )

