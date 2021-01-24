"""
Permissions to users
"""
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    class to owner permission
    """

    message = "No es el propietario"

    def has_object_permission(self, request, view, obj):
        """
        overwrite has_perimission method
        """

        # Verificar si el request está en la lista de métodos seguros como un
        # get.

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user == obj.owner:
            return True

        return False
