"""
views for users app
"""
from rest_framework import generics
from users.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    """
    User create view
    """
    serializer_class = UserSerializer
