from django.db import models
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import Users


class LoginSerializer(serializers.ModelSerializer):
    login = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        login = data.get("login")
        password = data.get("password")

        try:
            user = (Users.objects
                    .filter(models.Q(email=login) |
                            models.Q(nickname=login) |
                            models.Q(phone_number=login)
                            )
                    .get()
                    )
        except Users.DoesNotExits:
            raise serializers.ValidationError("Wrong login ")

        if not user.check_password(password):

            raise serializers.ValidationError("Wrong password")

        refresh = RefreshToken.for_user(user)
        data["user"] = user
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        return data
