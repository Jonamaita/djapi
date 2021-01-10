"""
Urls for users app
"""
from django.urls import path

from users.views import LoginView, UserCreate

urlpatterns = [
    path(
        "create/",
        UserCreate.as_view(),
        name="user_create",
    ),
    path("login/", LoginView.as_view(), name="login"),
]
