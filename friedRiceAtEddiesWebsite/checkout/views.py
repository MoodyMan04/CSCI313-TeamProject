from django.shortcuts import render, redirect
from checkout.models import CartItem
from main.models import Menu

# Create your views here.
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'checkout/checkout.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, item_id):
    item = Menu.objects.get(id=item_id)
    try:
        cart_item, created = CartItem.objects.get_or_create(item=item, user=request.user)
    except:
        cart_item, created = CartItem.objects.get_or_create(item=item)

    cart_item.quantity += 1
    cart_item.save()
    return redirect('/menu')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('/menu')
