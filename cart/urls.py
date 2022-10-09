from django.contrib import admin
from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path('cart', views.cart_view, name='cart-view'),
    path('clear-cart/', views.clear_cart, name='clear-cart'),
    path('delete/<id>/', views.delete_item, name='delete-item'),
    path('check-out', views.cart_check_out, name='cart-check-out'),
    path('update-item/', views.update_cart_Item, name='update-cart-Item'),
    path('order-porcess/', views.order_process, name='order-process'),
    path('pdf-invoice/<id>', views.render_pdf_invoice, name='render-pdf-invoice'),

]
