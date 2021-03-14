from django.dispatch.dispatcher import Signal
from order.models import Checkout
from inventory.models import Product

def update_product_quantity_handler(checkout:Checkout):
    product = checkout.product
    product.qty = product.qty - checkout.amount
    product.save()


Signal.connect(receiver=update_product_quantity_handler, sender=Checkout, dispatch_uid="update_product_quantity_handler")

