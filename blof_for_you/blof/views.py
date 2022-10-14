from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Blog, Category
from .forms import BlogForm


class HomeBlog(ListView):
    model = Blog
    context_object_name = 'news'
    paginate_by = 4

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
    allow_empty = False  # Запрещаем показ пустых списков
    paginate_by = 4

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
    context_object_name = 'news_item'  # Дефолтное название объекта


class CreateNews(CreateView):
    form_class = BlogForm
    template_name = 'blof/add_news.html'

