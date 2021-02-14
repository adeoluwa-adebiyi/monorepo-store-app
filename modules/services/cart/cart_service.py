from inventory.models import Product

class CartServiceContract(object):

    def get_total_items_and_total_price(self, cart_state=[]) -> tuple:
        pass


    def add_product_to_cart(self, product_id:int=None, amount:int=0, cart_state:dict=[]) -> tuple:
        pass


    def remove_cart_item(self, index:int=None, cart_state=[]) -> tuple:
        pass


    def update_cart_item(self, index:int=None, qty=0, cart_state=[]) -> tuple:
        pass


class CartService(CartServiceContract):

    INSTANCE = None

    @classmethod
    def instance(cls) -> CartServiceContract:
        if cls.INSTANCE == None:
            cls.INSTANCE = CartService()
        return cls.INSTANCE


    def get_total_items_and_total_price(self, cart_state=[]) -> tuple:

        total_items = 0

        total_price = 0

        for items in cart_state:
            total_items += items["amount"]
            total_price += items["price"]

        return total_items, total_price


    def add_product_to_cart(self, product_id:int=None, amount:int=0, cart_state:dict=[]) -> tuple:

        context = dict()

        product = Product.objects.get(id=product_id)

        cart_state = [
                *cart_state,
                {
                    "detail": {
                        "name": product.name,
                        "id": product.id,
                        "image": product.image,
                    },
                    "amount": amount,
                    "price": float(amount * product.price),
                }
            ]

        total_items, total_price = self.get_total_items_and_total_price(cart_state=cart_state)
        
        return total_items, total_price, cart_state


    def remove_cart_item(self, index:int=None, cart_state=[]) -> tuple:
        
        del cart_state[index]

        total_items, total_price = self.get_total_items_and_total_price(cart_state=cart_state)

        return total_items, total_price, cart_state


    def update_cart_item(self, index:int=None, qty=0, cart_state=[]) -> tuple:
        if index is not None and qty is not None:
            index = int(index)
            qty = int(qty)
            copy = cart_state
            product = Product.objects.get(id=cart_state[index]["detail"]["id"])
            copy[index]["amount"] = qty
            copy[index]["price"] = float(qty * product.price)
            cart_state = [
                *copy
            ]

            total_items, total_price = self.get_total_items_and_total_price(cart_state=cart_state)
            return total_items, total_price,cart_state
        else:
            raise Exception("Invalid Cart")

