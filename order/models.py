from django.db import models
from polymorphic.models import PolymorphicModel
from inventory.models import Product


OrderStatusChoices = [
    ("PENDING", "PENDING"),
    ("SATISFIED", "SATISFIED"),
    ("FAILED", "FAILED")
]


class Order(PolymorphicModel):

    id = models.AutoField(primary_key=True)
    status = models.CharField(choices=OrderStatusChoices, default="PENDING", max_length=10)
    checkout_id = models.CharField(max_length=50, null=False, blank=False)
    total_price = models.DecimalField(max_digits=20, decimal_places=8)
    delivery_address = models.ForeignKey("Address", null=True, on_delete=models.SET_NULL)


class Checkout(PolymorphicModel):

    id = models.AutoField(primary_key=True)
    checkout_id = models.CharField(max_length=50, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(null=False, blank=False)
    total_price = models.DecimalField(max_digits=20, decimal_places=8)


class Address(PolymorphicModel):

    id = models.AutoField(primary_key=True)


class DeliveryAddress(Address):

    post_code = models.CharField(max_length=6, null=True)


class Job(PolymorphicModel):
    id = models.AutoField(primary_key=True)


class TransactionJob(Job):
    order = models.ForeignKey("Order", null=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=OrderStatusChoices, max_length=10, default="PENDING")
    payment_data = models.JSONField()
