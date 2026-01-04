from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from booktracer.bookshelf.models.books import Book
from booktracer.users.models import Users


class BookComments(models.Model):
    author = models.ForeignKey(Users,
                               on_delete=models.CASCADE,
                               related_name="comment")
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
        ] )
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE)