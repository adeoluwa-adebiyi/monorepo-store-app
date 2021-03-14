from django.contrib import admin
from .models import Checkout, Order, TransactionJob

# Register your models here.

admin.site.register(Checkout)
admin.site.register(Order)
admin.site.register(TransactionJob)