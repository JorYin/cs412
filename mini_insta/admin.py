# File: admin.py
# Author: Jordan Yin (jordany@bu.edu), 09/27/2026
# Description: Administrative registration configuration for the mini_insta app models.

from django.contrib import admin
from .models import Profile, Post, Photo

# Register the Profile, Post, and Photo models with the Django admin interface.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)