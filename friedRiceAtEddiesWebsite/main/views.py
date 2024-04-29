from django.shortcuts import render
from main.models import Menu
import random, math

def index(request):
    menu_list =  Menu.objects.order_by('name')

    selected_items = random.sample(list(menu_list), math.floor(len(menu_list)/2))
    return render(request, 'main/index.html', {'menu': selected_items})

def menu(request):
    menu_list = Menu.objects.order_by('name')
    context = {'menu': menu_list}
    return render(request, 'main/menu.html', context=context)