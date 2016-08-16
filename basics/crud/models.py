from __future__ import unicode_literals

from django.db import models
from django import forms


# Create your models here.
class Purchases(models.Model):
    item_unique = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sold = models.IntegerField()
    price = models.DecimalField(max_length=7, decimal_places=2, max_digits=10)
    description = models.CharField(max_length=25)
    state = models.CharField(max_length=25)

    def __str__(self):
        return str(self.item_unique) + "," + self.name + "," + str(self.sold) + "," + str(self.price) \
               + "," + self.description + "," + self.state


class PurchasesForms(forms.Form):
    name = forms.CharField(max_length=50)
    sold = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(max_length=25)
    state = forms.CharField(max_length=25)
