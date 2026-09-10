# file: hw/urls.py

from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the hw app:
urlpatterns = [
  path(r'', views.quotes_quote_page, name='/'),
  path(r'quote', views.quotes_quote_page, name='quotes_quote'),
  path(r'show_all', views.quotes_show_all_page, name='quotes_show_all'),
  path(r'about', views.quotes_about_page, name='quotes_about')
]