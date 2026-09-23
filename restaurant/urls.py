# File: urls.py
# Author: Jordan Yin (jordany@bu.edu), 09/23/2026
# Description: Routing configuration mapping URL patterns to view functions for the restaurant app.

from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the restaurant app:
urlpatterns = [
    path(r'', views.main_restaurant, name="/"),
    path(r'main', views.main_restaurant, name="restaurant_main"),
    path(r'order', views.order_restaurant, name="restaurant_order"),
    path(r'submit', views.confirmation_restaurant, name="restaurant_confirmation"),
]