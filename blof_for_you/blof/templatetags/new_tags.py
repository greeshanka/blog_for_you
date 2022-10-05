from django import template
from django.db.models import Count, F

from blof.models import Category

register = template.Library()  #  Регистрация нашего тега


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {"categories": categories,
            }