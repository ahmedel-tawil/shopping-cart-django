import datetime

from django.db import models
from utilities.models import Customer
from products.models import Product


# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    finished = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_date = models.CharField(max_length=100, blank=True, null=True)

    def total_cart_price(self):
        return CartItems.cart_get_total(self.cartitems_set)

    def number_of_purchased_items(self):
        return CartItems.cart_get_number_of_items(self.cartitems_set)

    def get_paymenet_date(self):
        try:
            payment_date = datetime.datetime.fromtimestamp(float(self.payment_date))
            return str(payment_date)
        except:
            payment_date = 'Not paid yet!'
            return payment_date

    def __str__(self):
        return 'Cart ' + str(self.id)


# the model that send the signal to PRODUCT Model to update stock quantity
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    # getting Total price of Item


    @property
    def get_total(self):
        return self.quantity * self.product.product_price

    @staticmethod
    def cart_get_total(items):
        cart_total_price = items.aggregate(models.Sum('total_price'))['total_price__sum']
        return cart_total_price if cart_total_price else 0

    @staticmethod
    def cart_get_number_of_items(items):
        number_of_purchased_items = items.aggregate(models.Sum('quantity'))['quantity__sum']
        return number_of_purchased_items if number_of_purchased_items else 0

    def save(self, **kwargs):
        self.total_price = self.quantity * self.product.product_price
        super(CartItems, self).save(**kwargs)
