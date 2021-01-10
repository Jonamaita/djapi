"""
views for users app
"""
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    """
    User create view
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    """
    Manual Login
    """

    permission_classes = ()

    def post(self, request):
        """
        Post request
        """
        username = self.request.data.get("username")
        password = self.request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            return Response(
                {"token": user.auth_token.key},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "Bad credentials"},
            status=status.HTTP_400_BAD_REQUEST,
        )
