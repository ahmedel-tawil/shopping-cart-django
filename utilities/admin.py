from django.contrib import admin
from .models import Customer, PriceUnit, ItemUnit
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'view_order', 'view_paid_order', 'view_not_paid_order')


    def view_order(self, obj):
        count = obj.cart_set.count()
        url = (
                reverse("admin:cart_cart_changelist")
                + "?"
                + urlencode({"customer__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} # Orders</a>', url, count)

    view_order.short_description = "# Orders"

    def view_paid_order(self, obj):
        count = obj.cart_set.filter(finished=True).count()
        url = (
                reverse("admin:cart_cart_changelist")
                + "?"
                + urlencode({"customer__id": f"{obj.id}", "finished":True})
        )
        return format_html('<a href="{}">{} # Orders</a>', url, count)

    view_paid_order.short_description = "# Paid Orders"

    def view_not_paid_order(self, obj):
        count = obj.cart_set.filter(finished=False).count()
        url = (
                reverse("admin:cart_cart_changelist")
                + "?"
                + urlencode({"customer__id": f"{obj.id}", "finished":False})
        )
        return format_html('<a href="{}">{} # Orders</a>', url, count)

    view_not_paid_order.short_description = "# Not Paid Orders"



admin.site.register(Customer, CustomerAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('unit_symbol', 'unit_name')


admin.site.register(PriceUnit, CurrencyAdmin)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_symbol', 'unit_name')


admin.site.register(ItemUnit, UnitAdmin)
