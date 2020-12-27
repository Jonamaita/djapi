"""
Categroy admin classes.
"""
from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin class
    """

    list_display = ("description", "active")
