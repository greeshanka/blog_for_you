from django.urls import path
from blof.views import index, list_category


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', list_category, name='list_category'),
]