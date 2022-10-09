from django.shortcuts import render

from cart.models import Cart
from utilities.models import Customer
from .models import Product
# Create your views here.
def products_home(request):
    items = Product.objects.all()
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user,)
        # using get_or_create:
        cart , created = Cart.objects.get_or_create(customer=customer, finished=False)
        # Getting cart items attached to that cart
        cart_items = cart.cartitems_set.all()
        numbers_of_items = cart.number_of_purchased_items
    else:
        cart_items = []
        cart={}
        numbers_of_items = 0


    context={
        'items':items,
        'cart_items':cart_items,
        'numbers_of_items':numbers_of_items,
    }
    return render(request, 'products.html', context)
