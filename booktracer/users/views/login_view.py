from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.login_serializer import LoginSerializer


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["data"]
            access = serializer.validated_data["access"]
            refresh = serializer.validated_data["refresh"]

            return Response({
                "massage": "Logged in",
                "user_id": user.id,
                "nickname": user.nickname,
                "email": user.email,
                "phone_number": user.phone_number,
                "access": access,
                "refresh": refresh

        })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
