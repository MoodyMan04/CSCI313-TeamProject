from django.urls import path, include
from checkout import views

urlpatterns = [
    path('', views.view_cart, name='checkout'),
]