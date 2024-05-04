from django.shortcuts import render
from main.models import Menu
from main.models import Ingredient
from main.models import Recipe
from checkout.views import add_to_cart
import random, math

def index(request):
    menu_list =  Menu.objects.order_by('name')

    selected_items = random.sample(list(menu_list), math.floor(len(menu_list)/2))
    return render(request, 'main/index.html', {'menu': selected_items})

def menu(request):
    menu_list = Menu.objects.order_by('name')
    ingr_list = Ingredient.objects.order_by('name')
    recipe_list = Recipe.objects.order_by('menu_id').prefetch_related('ingredients')
    context = {'menu': menu_list, 'ingredients': ingr_list, 'recipes': recipe_list}
    return render(request, 'main/menu.html', context=context)

def add_button(request, item_id):
    return add_to_cart(request, item_id)
