from django.contrib import admin
from main import models as main_models
from checkout import models as checkout_models

# Register your models here.
@admin.register(main_models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Define admin class for Ingredient."""
    list_display = ('name', 'id')

@admin.register(main_models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Define admin class for Recipe."""
    list_display = ('id', 'menu_id')

@admin.register(main_models.Menu)
class MenuAdmin(admin.ModelAdmin):
    """Define admin class for Menu."""
    list_display = ('name', 'price', 'id')

@admin.register(checkout_models.Order)
class OrderAdmin(admin.ModelAdmin):
    """Define admin class for Order."""
    list_display = ('id', 'member_id', 'way_recieved_id', 'total', 'is_completed', 'is_cash')

@admin.register(checkout_models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """Define admin class for CheckoutItem."""
    list_display = ('user', 'item', 'quantity', 'date_added')

@admin.register(main_models.Way_Recieved)
class WayRecievedAdmin(admin.ModelAdmin):
    """Define admin class for WayRecieved."""
    list_display = ('type', 'id')

@admin.register(checkout_models.Member)
class MemberAdmin(admin.ModelAdmin):
    """Define admin class for Member."""
    list_display = ('username', 'fname', 'lname', 'phone_num', 'email', 'address', 'tokens', 'id')
