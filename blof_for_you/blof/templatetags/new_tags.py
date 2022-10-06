from django import template
from django.db.models import Count, F

from blof.models import Category

register = template.Library()  # Регистрация нашего тега


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('blof/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories,
            }
