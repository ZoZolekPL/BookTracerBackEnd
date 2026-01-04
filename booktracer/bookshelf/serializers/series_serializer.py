from rest_framework import serializers

from booktracer.bookshelf.models.series import BookSeries


class BookSeriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookSeries
        fields = ["name", "size","author","description"]