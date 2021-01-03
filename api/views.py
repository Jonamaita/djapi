"""
View for api app
"""

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductList(APIView):
    """
    Product list view
    """

    def get(self, request):
        """
        Get Method
        """
        products = Product.objects.all()[:20]
        data = ProductSerializer(products, many=True).data

        return Response(data)


class ProductDetail(APIView):
    """
    Product detail view
    """
    def get(self, request, pk):  # pylint:disable=invalid-name
        """
        Get method
        """
        product = get_object_or_404(Product, pk=pk)
        data = ProductSerializer(product).data

        return Response(data)
