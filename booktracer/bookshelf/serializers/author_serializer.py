from rest_framework import serializers

from booktracer.bookshelf.models.authors import Authors


class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = ["nickname","name","last_name","death_date","description","sex","country"]
