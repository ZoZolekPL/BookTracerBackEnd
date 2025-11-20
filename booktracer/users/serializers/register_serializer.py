from rest_framework import serializers

from ..models import Users


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["nickname", "password", "email", "name", "last_name", "phone_number", "avatar"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Users(**validated_data)
        user.save()
        return user
