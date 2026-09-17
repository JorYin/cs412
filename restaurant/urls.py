# file: restaurant/urls.py

from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the hw app:
urlpatterns = [
    path(r'', views.main_restaurant, name="/"),
    path(r'main', views.main_restaurant, name="restaurant_main"),
    path(r'order', views.order_restaurant, name="restaurant_order"),
    path(r'submit', views.confirmation_restaurant, name="restaurant_confirmation"),
]