from django.db import models

from .authors import Authors
from .genre import Genre
from .series import BookSeries


class Book(models.Model):

    def book_image(instance, filename):
        return f"book_{instance.book.id}/{filename}"

    title = models.CharField(max_length=256)
    author = models.ForeignKey(Authors,
                               on_delete=models.CASCADE,
                               related_name="Author"
    )
    size = models.DecimalField(max_digits=200, decimal_places=0)
    genre = models.ForeignKey(Genre,
                              on_delete=models.CASCADE,
                              related_name="genres")
    series = models.ForeignKey(BookSeries,
                               on_delete=models.CASCADE)
    series_number = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    isbn_code = models.DecimalField(max_digits=13, decimal_places=0)
    image = models.ImageField(upload_to=book_image)

