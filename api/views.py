"""
View for api app
"""

# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics

from .models import Category, Product, SubCategory
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    SubCategorySerializer,
)

# # Class based views
# class ProductList(APIView):
#     """
#     Product list view
#     """

#     def get(self, request):
#         """
#         Get Method
#         """
#         products = Product.objects.all()[:20]
#         data = ProductSerializer(products, many=True).data

#         return Response(data)


# class ProductDetail(APIView):
#     """
#     Product detail view
#     """
#     def get(self, request, pk):  # pylint:disable=invalid-name
#         """
#         Get method
#         """
#         product = get_object_or_404(Product, pk=pk)
#         data = ProductSerializer(product).data

#         return Response(data)

# Generics views class
class ProductList(generics.ListCreateAPIView):
    """
    Product list view
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveDestroyAPIView):
    """
    Product detail view
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    """
    Category list view
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryList(generics.ListCreateAPIView):
    """
    SubCategory List view
    """

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


# Generics view for only create object (not in use)
class CategorySave(generics.CreateAPIView):
    """
    Category save view. Only for create category
    """

    serializer_class = CategorySerializer


class SubCategorySave(generics.CreateAPIView):
    """
    SubCategory save view. Only for create subcategory
    """

    serializer_class = SubCategorySerializer


class CategoryDetail(generics.RetrieveDestroyAPIView):
    """
    Category detail
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryCategory(generics.ListCreateAPIView):
    """
    List all subcategories of a category
    """

    # Sobreescribimos la query set, para filtrar las subcategoria por categoria
    def get_queryset(self):
        queryset = SubCategory.objects.all().filter(
            category_id=self.kwargs["pk"]
        )

        return queryset

    serializer_class = SubCategorySerializer
