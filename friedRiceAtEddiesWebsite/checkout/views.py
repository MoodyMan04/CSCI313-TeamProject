from django.shortcuts import render, redirect
from django.contrib import messages
from checkout.models import CartItem, Order, Member, OrderLine
from main.models import Menu, Way_Recieved
import math

# Create your views here.
def view_cart(request):
    try:
        cart_items = CartItem.objects.filter(user=Member.objects.get(user=request.user))
        member = Member.objects.get(user=request.user)
        tokens = member.tokens
    except:
        cart_items = CartItem.objects.filter(user=None)
        tokens = 0
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    way_recieveds = Way_Recieved.objects.all
    
    return render(request, 'checkout/checkout.html', {'cart_items': cart_items, 'total_price': total_price, 
                                                      'tax': round((float(total_price) * 0.0697), 2), 
                                                      'final_price': float(total_price) + round((float(total_price) * 0.0697), 2),
                                                      'way_recieveds': way_recieveds, 'tokens': tokens})

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
        cart_item, created = CartItem.objects.get_or_create(item=item, user=Member.objects.get(user=request.user))
    except:
        cart_item, created = CartItem.objects.get_or_create(item=item)

    cart_item.quantity += 1
    cart_item.save()
    return redirect('/checkout')

def add_custom_to_cart(request):
    items = Menu.objects.all()

    item_to_use = ''
    for item in items:
        if item.name == 'Custom item':
            item_to_use = item
    try:
        cart_item, created = CartItem.objects.get_or_create(item=item, user=Member.objects.get(user=request.user))
    except:
        cart_item, created = CartItem.objects.get_or_create(item=item)

    cart_item.quantity += 1
    cart_item.save()
    return redirect('/checkout')

def remove_from_cart(request, item_id):
    item = Menu.objects.get(id=item_id)
    try:
        cart_item = CartItem.objects.filter(user=Member.objects.get(user=request.user)).get(item=item)
    except:
        cart_item = CartItem.objects.filter(user=None).get(item=item)
    cart_item.delete()
    return redirect('/checkout')

def process_order(request, w_id):
    member = None
    try:
        cart_items = CartItem.objects.filter(user=Member.objects.get(user=request.user))
        member = Member.objects.get(user=request.user)
    except:
        cart_items = CartItem.objects.filter(user=None)
    try:
        total_price = float(sum(item.item.price * item.quantity for item in cart_items))    
    except:
        total_price = 0

    if (total_price>0):#prevent empty orders
        total_price+=total_price*0.0697
        messages.success(request, f'{Way_Recieved.objects.get(id=w_id)} order placed! Your total is: ${round(float(total_price), 2)}. Thank you for the gold, {member if member is not None else "kind stranger"}!')
        order = Order.objects.create(member_id=member, way_recieved_id = Way_Recieved.objects.get(id=w_id), total=total_price, is_completed=False, is_cash=False)
        if (member != None): #Set tokens
            new_tokens = round(float(total_price), 2)*100
            member.tokens += new_tokens
            member.save()

        for i in cart_items: #Clear cart and add to order
            line = OrderLine.objects.get_or_create(menu_item=i.item, qty=i.quantity)
            order.menu_items.add(line[0])
            i.delete()
    else:
        messages.error(request, 'Order failed: no items in cart.')

    
    return redirect('/checkout')
