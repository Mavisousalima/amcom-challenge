from django.db import models

from clients.models import Client
from sellers.models import Seller
from products.models import Product


class Sale(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    date_time = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='SaleItem')


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()