"""
urls for api app
"""
from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path(
        "v1/product_list/",
        ProductList.as_view(),
        name="product_list"
    ),
    path(
        "v1/product/<int:pk>",
        ProductDetail.as_view(),
        name="product_detail"
    ),
]
