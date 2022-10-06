from django.urls import path
from blof.views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', list_category, name='list_category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add_news/', add_news, name='add_news'),

]