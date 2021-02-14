from django.urls import path
from .views import CategoryProductListingView, ProductInformationView


urlpatterns =[
    path("category/view/<str:category>/<str:sub_category>/<int:page>", CategoryProductListingView.as_view()),
    path("product/view/<int:product_id>", ProductInformationView.as_view())
]