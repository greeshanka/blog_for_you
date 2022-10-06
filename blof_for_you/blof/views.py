from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog, Category
from .forms import BlogForm


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


def view_news(request, news_id):
    news_item = get_object_or_404(Blog, pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request, template_name='blof/news_item.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = BlogForm()
    return render(request, template_name='blof/add_news.html', context={'form': form})
