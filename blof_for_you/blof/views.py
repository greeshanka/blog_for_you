from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

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


class CategoryListBlog(ListView):
    model = Blog
    context_object_name = 'news'  # Деволтное название объекта
    # allow_empty = False  # Запрещаем показ пустых списков

    def get_context_data(self, *, object_list=None, **kwargs):
        """Метод объединяет(сливает вместе) данные контекста всех родительских классов с данными текущего класса """
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        """Метод для фильтрации данных"""
        return Blog.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = Blog
    # pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'  # Деволтное название объекта


def add_news(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = BlogForm()
    return render(request, template_name='blof/add_news.html', context={'form': form})
