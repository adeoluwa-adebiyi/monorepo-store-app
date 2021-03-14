from order.models import Order, Checkout

class OrderServiceContract(object):

    def __init__(self):
        pass

    def create_order(self, checkout_id:str) -> Order:
        pass


class OrderService(OrderServiceContract):

    def create_order(self, checkout_id: str) -> Order:
        total_price = 0
        checkouts = Checkout.objects.filter(checkout_id=checkout_id)
        for checkout in checkouts:
            total_price += checkout.total_price
        return Order.objects.create(total_price=total_price)