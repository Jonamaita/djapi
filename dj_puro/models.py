"""
    Models dj_puro app
"""
from django.db import models


class Category(models.Model):
    """
    Category Model
    """

    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
