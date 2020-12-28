"""
Categroy admin classes.
"""
from django.contrib import admin
from .models import Category, SubCategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin class
    """

    list_display = ("description",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """
    SubCategory Admin class
    """

    list_display = ("category", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product Admin class
    """

    list_display = ("subcategory", "description", "sold")
