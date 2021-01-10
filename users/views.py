"""
views for users app
"""
from rest_framework import generics

from users.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    """
    User create view
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
