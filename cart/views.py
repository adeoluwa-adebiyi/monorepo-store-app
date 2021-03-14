from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView
from django.shortcuts import render
from inventory.models import Product
from django.http.request import HttpRequest
from modules.services.cart.cart_service import CartService
from django.http.response import HttpResponse


class AddProductToCardView(View):

    def post(self, request: HttpRequest, product_id):

        amount = int(request.POST.get("amount"))

        total_items, total_price, cart_state = CartService.instance().add_product_to_cart(\
            product_id=product_id, amount=amount, cart_state=request.session.get("cart",[]))

        request.session["cart"] = cart_state
        request.session["cart_total_items"] = total_items
        request.session["cart_total_price"] = total_price

        return redirect("/")


class RemoveProductFromCartView(View):

    def get(self, request):

        index = int(request.GET.get("index"))

        total_items, total_price, cart_state = CartService.instance().\
            remove_cart_item(index=index, cart_state=request.session.get("cart", []))

        request.session["cart"] = cart_state
        request.session["cart_total_items"] = total_items
        request.session["cart_total_price"] = total_price

        return redirect("/cart/view")


class ViewCartView(View):

    def get(self, request):

        template_name = "cart_listing.html"

        try:

            index = request.GET.get("update")

            qty = request.GET.get("qty")

            if index is not None and qty is not None:

                total_items, total_price, cart_state = CartService.instance().update_cart_item(index=index, qty=qty,cart_state=request.session.get("cart",[]))

                request.session["cart"] = cart_state
                request.session["cart_total_items"] = total_items
                request.session["cart_total_price"] = total_price

            return render(request, template_name)
        except Exception as e:
            return HttpResponse(str(e))
