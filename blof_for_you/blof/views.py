from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Blog, Category
from .forms import BlogForm


class HomeBlog(ListView):
    model = Blog
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Метод объединяет(сливает вместе) данные контекста всех родительских классов с данными текущего класса """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        """Метод для фильтрации данных. Корректировка запроса под получение данных"""
        return Blog.objects.filter(is_published=True).select_related('category')


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
