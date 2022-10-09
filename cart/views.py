import datetime
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
import json
from .models import *
from xhtml2pdf import pisa


# Create your views here.
def cart_view(request):
    customer = request.user.customer
    # using get_or_create:
    cart, created = Cart.objects.get_or_create(customer=customer, finished=False)
    # Getting cart items attached to that cart
    cart_items = cart.cartitems_set.all()
    numbers_of_items = cart.number_of_purchased_items

    context = {
        'cart_items': cart_items,
        'numbers_of_items': numbers_of_items,
        'cart': cart,
    }
    return render(request, 'cart.html', context)


def update_cart_Item(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']
    print('Action:', action)
    print('Item:', itemId)
    customer = request.user.customer
    item = Product.objects.get(id=itemId)
    cart, created = Cart.objects.get_or_create(customer=customer, finished=False)
    cartitem, created = CartItems.objects.get_or_create(cart=cart, product=item)

    if action == 'add':
        if cartitem.product.available_qty > cartitem.quantity:
            cartitem.quantity = (cartitem.quantity + 1)
            messages.success(request, 'your cart now contains ' + str(cartitem.quantity) + ' ' + str(
                cartitem.product.unit) + ' of ' + str(cartitem.product.product_name))
        else:
            messages.warning(request, 'There is only ' + str(cartitem.product.available_qty) + ' ' + str(
                cartitem.product.unit) + ' of ' + str(cartitem.product.product_name) + ' left in stock')
    elif action == 'remove':
        cartitem.quantity = (cartitem.quantity - 1)
        messages.info(request, 'your cart now contains ' + str(cartitem.quantity) + ' ' + str(
            cartitem.product.unit) + ' of ' + str(cartitem.product.product_name))
    cartitem.save()

    if cartitem.quantity <= 0:
        messages.error(request, 'The ' + str(
            cartitem.product.product_name) + ' will be deleted form your cart, if you wish to order this item again, please press continue shopping')
        cartitem.delete()
    return JsonResponse('Item Added to the cart', safe=False)


def clear_cart(request):
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer, finished=False)
    cart_items = cart.cartitems_set.all()
    cart_items.delete()
    return redirect('cart:cart-view')


def delete_item(request, id):
    cart_item = CartItems.objects.get(id=id)
    cart_item.delete()
    return redirect('cart:cart-view')


def cart_check_out(request):
    # checking user authentication
    customer = request.user.customer
    # using get_or_create:
    cart, created = Cart.objects.get_or_create(customer=customer, finished=False)
    # Getting cart items attached to that cart
    cart_items = cart.cartitems_set.all()

    numbers_of_items = cart.number_of_purchased_items

    context = {
        'cart_items': cart_items,
        'numbers_of_items': numbers_of_items,
        'cart': cart,
    }
    return render(request, 'check-out.html', context)


def order_process(request):
    payment_date = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer, finished=False)
    cart.payment_date = payment_date
    cart.finished = True
    cart.save()
    return JsonResponse('Order Completed.. thank you', safe=False)


def render_pdf_invoice(request, id):
    template_src = 'pdf-invoice.html'
    customer = request.user.customer
    cart = Cart.objects.get(id=id)
    cart_items = cart.cartitems_set.all()
    payment_date = datetime.datetime.now()

    context = {
        'customer':customer,
        'cart_items': cart_items,
        'payment_date': payment_date,
        'cart': cart,
    }
    pdf_name = str(customer.user.first_name) + ' ' + str(customer.user.last_name) + ' # invoice -' + str(cart.id)+'.pdf'
    template = get_template(template_src)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf_name}"'
    pdf = pisa.CreatePDF(html, dest=response)
    if pdf.err:
        return messages.error(request, 'Cannot Download Your invoice right now ')

    return response
