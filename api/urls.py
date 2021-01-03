"""
urls for api app
"""
from django.urls import path

from .views import CategorySave, ProductDetail, ProductList, SubCategorySave

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
        CategorySave.as_view(),
        name="category_save",
    ),
    path(
        "v1/subcategory/",
        SubCategorySave.as_view(),
        name="subcategory_save",
    ),
]
