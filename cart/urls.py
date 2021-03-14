from django.urls import path
from .views import AddProductToCardView, RemoveProductFromCartView, ViewCartView


urlpatterns = [
    path("add/<int:product_id>", AddProductToCardView.as_view()),
    path("remove", RemoveProductFromCartView.as_view()),
    path("view", ViewCartView.as_view())
]