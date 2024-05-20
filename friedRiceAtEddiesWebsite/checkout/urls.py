from django.urls import path
from checkout import views

urlpatterns = [
    path('', views.view_cart, name='checkout'),
    path('remove_from_cart/<item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('process_order/<w_id>', views.process_order, name='process_order'),
    path('menu/add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('menu/add_to_cart/', views.add_custom_to_cart, name='add_custom_to_cart'),
]