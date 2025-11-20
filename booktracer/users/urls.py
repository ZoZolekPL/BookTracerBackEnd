from django.urls import path

from .views.login_view import LoginAPIView
from .views.register_view import RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
]
