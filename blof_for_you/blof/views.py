from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog


def index(request):
    news = Blog.objects.all()
    return render(request, template_name='blof/index.html', context={'news': news, 'title': 'Список новостей'})
