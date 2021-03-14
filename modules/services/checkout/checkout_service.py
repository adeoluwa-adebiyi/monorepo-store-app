from uuid import uuid4
from order.models import Checkout
from inventory.models import Product
from modules.exceptions.checkout_exceptions import InsufficientProductQuantityError


class CheckoutServiceContract(object):

    def __init__(self):
        pass

    def checkout(cart: list) -> str:
        pass


class CheckoutService(CheckoutServiceContract):

    def __init__(self):
        pass

    #Cart item model
    # {
    #             "detail": {
    #                 "name": product.name,
    #                 "id": product.id,
    #                 "image": product.image,
    #             },
    #             "amount": amount,
    #             "price": float(amount * product.price),
    #         }

    #Checkout model params:
    # checkout_id = models.CharField(max_length=50, null=False, blank=False)
    # product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True),
    # amount = models.IntegerField(null=False, blank=False)
    # total_price = models.DecimalField(max_digits=20, decimal_places=8)

    def checkout(self,cart: list) -> str:

        checkout_id = self.__generate_unique_checkout_id()

        for item in cart:

            prod_id, amount, price = item["detail"]["id"], item["amount"], item["price"]
            product = Product.objects.get(id=prod_id)

            if amount > product.qty:
                raise InsufficientProductQuantityError(f"Selected quantity for {product} more than available qty: {product.qty}")
                break

            checkout = Checkout.objects.create(checkout_id=checkout_id, product=product, amount=amount, total_price=price)

        return checkout_id


    def __generate_unique_checkout_id(self):
        checkout_id = None
        while True:
            _id = uuid4()
            ids = Checkout.objects.filter(checkout_id=_id)
            if len(ids) == 0:
                checkout_id = _id
                break
        return checkout_id
