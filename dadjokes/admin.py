# File: admin.py
# Author: Jordan Yin (jordany@bu.edu), 11/10/2026
# Description: Registers Dad Jokes models with the Django admin site.

from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Joke)
admin.site.register(Picture)