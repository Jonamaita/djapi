"""
urls for api app
"""
from django.urls import path

from .views import CategoryList, ProductDetail, ProductList, SubCategoryList

urlpatterns = [
    path(
        "v1/products/",
        ProductList.as_view(),
        name="product_list",
    ),
    path(
        "v1/product/<int:pk>",
        ProductDetail.as_view(),
        name="product_detail",
    ),
    path(
        "v1/category/",
        CategoryList.as_view(),
        name="category_list",
    ),
    path(
        "v1/subcategory/",
        SubCategoryList.as_view(),
        name="subcategory_list",
    ),
]
