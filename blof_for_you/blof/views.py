from django.shortcuts import render

from .models import Blog, Category


def index(request):
    news = Blog.objects.all()
    context = {
        'news': news,
    }
    return render(request, template_name='blof/index.html', context=context)


def list_category(request, category_id):
    news = Blog.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, template_name='blof/category.html', context=context)
