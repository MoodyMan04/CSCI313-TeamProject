from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('menu/add_button/<item_id>', views.add_button, name='add_button'),
]