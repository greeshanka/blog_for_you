from django.urls import path
from blof.views import *


urlpatterns = [
    path('', HomeBlog.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryListBlog.as_view(), name='list_category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', add_news, name='add_news'),

]