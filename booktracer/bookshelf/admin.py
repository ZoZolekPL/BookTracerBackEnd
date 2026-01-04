from django.contrib import admin

from .models.authors import Authors
from .models.books import Book
from .models.genre import Genre
from .models.series import BookSeries

# Register your models here.

admin.site.register(Genre)
admin.site.register(BookSeries)
admin.site.register(Authors)
admin.site.register(Book)