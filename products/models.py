from django.db import models

from utilities.models import PriceUnit, ItemUnit


# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category Type')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Category Description')

    class Meta:
        verbose_name_plural = 'Category List'

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Product Name')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_category',
                                 verbose_name='Product Category')
    product_price = models.FloatField(verbose_name='unit price')
    price_currency = models.ForeignKey(PriceUnit, on_delete=models.CASCADE, verbose_name='Currency')
    unit = models.ForeignKey(ItemUnit, on_delete=models.CASCADE, verbose_name='Unit')
    available_qty = models.FloatField(default=0, verbose_name='Available Quantity')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Product Description')
    product_image = models.ImageField(upload_to='products/images', blank=True, null=True, verbose_name='Product Image')

    def __str__(self):
        return self.product_name

