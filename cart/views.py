from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView
from django.shortcuts import render
from inventory.models import Product
from django.http.request import HttpRequest


class AddProductToCardView(View):

    def post(self, request: HttpRequest, product_id):

        amount = int(request.POST.get("amount"))

        context = dict()

        product = Product.objects.get(id=product_id)

        request.session["cart"] = [
            *request.session.get("cart", []),
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

        total_items = 0

        total_price = 0

        for items in request.session.get("cart",[]):
            total_items += items["amount"]
            total_price += items["price"]

        request.session["cart_total_items"] = total_items
        request.session["cart_total_price"] = total_price

        return redirect("/")


class RemoveProductFromCartView(View):

    def get(self, request):

        context = dict()

        index = int(request.GET.get("index"))

        cart_state = request.session.get("cart")

        del cart_state[index]

        request.session["cart"] = cart_state

        total_items = 0

        total_price = 0

        for items in request.session.get("cart",[]):
            total_items += items["amount"]
            total_price += items["price"]

        request.session["cart_total_items"] = total_items
        request.session["cart_total_price"] = total_price

        return redirect("/cart/view")


class ViewCartView(View):

    def get(self, request):

        template_name = "cart_listing.html"

        index = request.GET.get("update")

        qty = request.GET.get("qty")

        
        if index is not None and qty is not None:
            index = int(index)
            qty = int(qty)
            copy = request.session["cart"]
            product = Product.objects.get(id=request.session["cart"][index]["detail"]["id"])
            copy[index]["amount"] = qty
            copy[index]["price"] = float(qty * product.price)
            request.session["cart"] = [
                *copy
            ]

            total_items = 0

            total_price = 0

            for items in request.session.get("cart",[]):
                total_items += items["amount"]
                total_price += items["price"]

            request.session["cart_total_items"] = total_items
            request.session["cart_total_price"] = total_price

        return render(request, template_name)
