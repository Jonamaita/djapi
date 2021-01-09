"""
urls for api app
"""
from django.urls import path
from rest_framework import routers

from .views import (
    AddSubCategory,
    CategoryDetail,
    CategoryList,
    ProductDetail,
    ProductList,
    ProductViewSet,
    SubCategoryCategory,
    SubCategoryList,
)

# Cojunto de vista para products
router = routers.DefaultRouter()
router.register(r"v2/products", ProductViewSet, basename="product")

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
    # Agregar Subcategoria
    path(
        "v1/category/<int:cat_pk>/addsubcategory/",
        AddSubCategory.as_view(),
        name="add_subcategory",
    ),
]

urlpatterns += router.urls
