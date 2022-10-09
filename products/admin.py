from django.contrib import admin
from django.db.models import Sum
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','view_products')

    def view_products(self, obj):
        count = obj.product_category.count()
        url = (
                reverse("admin:products_product_changelist")
                + "?"
                + urlencode({"category__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} # Products</a>', url, count)

    view_products.short_description = "# Products"


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'available_qty', 'product_price', 'qty_sold', 'total_price')
    list_filter = ('category',)


    def qty_sold(self, obj):
        qty_sold = obj.cartitems_set.aggregate(qty=Sum('quantity'))['qty']
        unit = obj.unit
        url = (
                reverse("admin:cart_cartitems_changelist")
                + "?"
                + urlencode({"product__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}  {}</a>', url, qty_sold , unit)

    qty_sold.short_description = "# Quantity Sold"

    def total_price(self, obj):
        price = obj.cartitems_set.aggregate(price=Sum('total_price'))['price']
        unit = obj.price_currency
        url = (
                reverse("admin:cart_cartitems_changelist")
                + "?"
                + urlencode({"product__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}  {}</a>', url, price , unit)

    total_price.short_description = "Total Price"

admin.site.register(Product, ProductAdmin)
