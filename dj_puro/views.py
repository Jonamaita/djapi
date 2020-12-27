"""
    Views to dj_puro app
"""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Category


def category_list(request):
    """
    Category list view
    """
    max_objects = 20
    cat = Category.objects.all()[:max_objects]
    data = {"results": list(cat.values("description", "active"))}

    return JsonResponse(data)


def category_detail(request, pk):
    """
    Category detail view
    """
    # pylint: disable=invalid-name

    cat = get_object_or_404(Category, pk=pk)
    data = {
        "results": {
            "description": cat.description,
            "active": cat.active,
        }
    }

    return JsonResponse(data)
