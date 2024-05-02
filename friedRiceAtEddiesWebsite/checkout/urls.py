from django.urls import path, include
from checkout import views

urlpatterns = [
    path('', views.view_cart, name='checkout'),
    path('remove_from_cart/<item_id>', views.remove_from_cart, name='remove_from_cart')
]