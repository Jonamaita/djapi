"""
Serializers for api app.
"""
from rest_framework import serializers

from .models import Category, Product, SubCategory


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for product model.
    """

    # agregamos el field owner como oculto y agregamos el valor por defecto
    # al usuario que esta logueado en ese momento
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category model.
    """

    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for subcategory model.
    """

    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = SubCategory
        fields = "__all__"
