"""
    Models api app
"""
from django.db import models
from django.conf import settings


class OwnerModel(models.Model):
    """
    Class owner

    Es una clase abstracta, quiere decir que no se generará como un modelo.
    El campo owner e agregará al modelo que herede esta clase.
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class Category(OwnerModel):
    """
    Category Model
    """

    description = models.CharField(
        max_length=100,
        help_text="Category Description",
        unique=True,
    )

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(OwnerModel):
    """
    Category Model
    """

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100,
        help_text="SubCategory Description",
        unique=True,
    )

    def __str__(self):
        return f"{self.category.description}:{self.description}"

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"
        unique_together = ("category", "description")


class Product(OwnerModel):
    """
    Product Model
    """

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100,
        help_text="Product Description",
        unique=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
