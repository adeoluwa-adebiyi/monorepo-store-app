from django.urls import path, include
from .views import HomePageTemplateView

urlpatterns = [
    path("", HomePageTemplateView.as_view(), name="home")
]