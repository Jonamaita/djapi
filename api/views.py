"""
View for api app
"""

# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

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
