"""
Serializers for api app.
"""
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for product model.
    """

    class Meta:
        model = Product
        fields = "__all__"
