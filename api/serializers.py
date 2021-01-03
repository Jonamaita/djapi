"""
Serializers for api app.
"""
from rest_framework import serializers

from .models import Category, Product, SubCategory


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for product model.
    """

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category model.
    """

    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for subcategory model.
    """

    class Meta:
        model = SubCategory
        fields = "__all__"
