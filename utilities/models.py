from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='customers_user', null=True, blank=True)

    def __str__(self):
        return 'account: ' +str(self.user) +',  Name: ' + ((str(self.user.first_name) + ' ' +str(self.user.last_name) ) if self.user.first_name and self.user.last_name else 'No Name assigned!')




class PriceUnit(models.Model):
    unit_symbol = models.CharField(max_length=10)
    unit_name = models.CharField(max_length=50)

    def __str__(self):
        return self.unit_symbol


class ItemUnit(models.Model):
    unit_symbol = models.CharField(max_length=10)
    unit_name = models.CharField(max_length=50)

    def __str__(self):
        return self.unit_symbol
