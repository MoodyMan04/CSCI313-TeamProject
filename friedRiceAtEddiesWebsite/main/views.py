from django.shortcuts import render
from main.models import Menu

def index(request):
    return render(request, 'main/index.html')

def menu(request):
    menu_list = Menu.objects.order_by('name')
    context = {'menu': menu_list}
    return render(request, 'main/menu.html', context=context)