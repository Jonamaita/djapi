"""
    urls for dj_puro app
"""
from django.urls import path
from .views import category_list, category_detail

urlpatterns = [
    path("categories/", category_list, name="category_list"),
    path("category/<int:pk>", category_detail, name="category_detail"),

]
