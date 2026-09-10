# file: hw/urls.py

from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the hw app:
urlpatterns = [
  path(r'', views.quote_page, name='/'),
  path(r'', views.quote_page, name='quote'),
  path(r'', views.show_all_page, name='show_all'),
  path(r'', views.about_page, name='about')
]