
from django.db.models.signals import post_save
from django.dispatch import receiver

from cart.models import CartItems, Cart
from products.models import Product

@receiver(post_save, sender=Cart)
def update_item(sender, instance, created, **kwargs):
    if instance.finished:
        items_bought = instance.cartitems_set.all()
        for x in items_bought:
            item_to_update = Product.objects.get(id=x.product.id)
            print('product name ', x.product.product_name,' availble-qty ',item_to_update.available_qty, ' quantity-purchased ', x.quantity)
            item_to_update.available_qty = item_to_update.available_qty-x.quantity
            item_to_update.save()
            print('Stock level updated...')





#post_save.connect(update_item, sender=CartItems)
