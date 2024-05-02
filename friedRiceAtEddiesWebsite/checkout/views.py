from django.shortcuts import render, redirect
from checkout.models import CartItem
from main.models import Menu

# Create your views here.
def view_cart(request):
    try:
        cart_items = CartItem.objects.filter(user=request.user)
    except:
        cart_items = CartItem.objects.filter(user=None)
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    return render(request, 'checkout/checkout.html', {'cart_items': cart_items, 'total_price': total_price, 
                                                      'tax': round((float(total_price) * 0.0697), 2), 
                                                      'final_price': float(total_price) + round((float(total_price) * 0.0697), 2)})

# def total_items_cart(request):
#     try:
#         cart_items = CartItem.objects.filter(user=request.user)
#     except:
#         cart_items = CartItem.objects.filter(user=None)
#     total_items = sum(item.quantity for item in cart_items)
#     return total_items

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
    item = Menu.objects.get(id=item_id)
    try:
        cart_item = CartItem.objects.filter(user=request.user).get(item=item)
    except:
        cart_item = CartItem.objects.filter(user=None).get(item=item)
    cart_item.delete()
    return redirect('/checkout')
