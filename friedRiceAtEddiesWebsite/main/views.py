from django.shortcuts import render
from main.models import Menu
from main.models import Ingredient
from main.models import Recipe

def index(request):
    return render(request, 'main/index.html')

def menu(request):
    menu_list = Menu.objects.order_by('name')
    ingr_list = Ingredient.objects.order_by('name')
    recipe_list = Recipe.objects.order_by('menu_id').prefetch_related('ingredients')
    context = {'menu': menu_list, 'ingredients': ingr_list, 'recipes': recipe_list}
    return render(request, 'main/menu.html', context=context)
