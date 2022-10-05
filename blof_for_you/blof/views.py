from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog, Category


def index(request):
    news = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, template_name='blof/index.html', context=context)


def list_category(request, category_id):
    news = Blog.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category,
    }
    return render(request, template_name='blof/category.html', context=context)
