from django.contrib import admin
from .models import *
# Register your models here.

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer',Cart.number_of_purchased_items, Cart.total_cart_price , 'finished', Cart.get_paymenet_date )
    fields = ('customer', 'payment_date')
    list_filter = ('customer', 'finished')
    date_hierarchy = 'updated_at'

admin.site.register(Cart, CartAdmin)

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price' , 'created_date')
    list_filter = ('product', )
admin.site.register(CartItems, CartItemsAdmin )
