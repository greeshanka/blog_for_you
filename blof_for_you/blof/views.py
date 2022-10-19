from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Category
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gooooood!')
            return redirect('login')
        else:
            messages.error(request, 'WTF?!')

    else:
        form = UserRegisterForm()
    return render(request, 'blof/register.html', context={'form': form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, 'blof/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


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
