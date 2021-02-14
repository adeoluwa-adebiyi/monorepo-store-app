def cart_context(request):

    return {
        "cart" : request.session.get("cart", []),
        "cart_total_items": request.session.get("cart_total_items", 0),
        "cart_total_price": request.session.get("cart_total_price", 0)
    }