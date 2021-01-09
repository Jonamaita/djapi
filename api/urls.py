"""
urls for api app
"""
from django.urls import path

from .views import (
    CategoryDetail,
    CategoryList,
    ProductDetail,
    ProductList,
    SubCategoryList,
    SubCategoryCategory,
)

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
    path(
        "v1/category/<int:pk>",
        CategoryDetail.as_view(),
        name="category_list",
    ),
    # Listar las subcategorias de una categoria
    path(
        "v1/category/<int:pk>/subcategory/",
        SubCategoryCategory.as_view(),
        name="subcategory_category_list",
    ),
]
