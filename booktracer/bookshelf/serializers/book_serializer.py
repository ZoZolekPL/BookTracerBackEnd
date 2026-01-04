from rest_framework import serializers

from booktracer.bookshelf.models.books import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["tittle","author","size","genre",
                  "series","series_number","description",
                  "isbn_code","image"]