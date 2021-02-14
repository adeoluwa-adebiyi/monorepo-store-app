from django.urls import path
from .views import CheckoutCartView, PayTransactionView, AuthorizeOtpView


urlpatterns = [
    path("checkout", CheckoutCartView.as_view(), name="checkout-cart-view"),
    path("pay/<int:order_id>", PayTransactionView.as_view(), name="payment-view"),
    path("authorize/<int:trxjob_id>", AuthorizeOtpView.as_view(), name="authorize-otp-view")
]