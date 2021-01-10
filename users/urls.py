"""
Urls for users app
"""
from django.urls import path
from users.views import UserCreate

urlpatterns = [
    path(
        "create/",
        UserCreate.as_view(),
        name="user_create",
    )
]
