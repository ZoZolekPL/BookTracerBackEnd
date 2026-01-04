from rest_framework import serializers

from booktracer.bookshelf.models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ["name", "description",]
