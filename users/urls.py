"""
Urls for users app
"""
from django.urls import path

# Vista de autenticación por defecto de Drf
from rest_framework.authtoken import views

from users.views import LoginView, UserCreate

urlpatterns = [
    path("create/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    # Autenticación con la vista por defecto de Drf
    path("login-drf/", views.obtain_auth_token, name="login-drf"),
]
