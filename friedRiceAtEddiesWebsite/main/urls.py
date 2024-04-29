from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
]