# news/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category>/', views.category_view, name='category'),
    path('search/', views.search, name='search'),
]
