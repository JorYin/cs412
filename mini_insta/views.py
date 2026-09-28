# File: views.py
# Author: Jordan Yin (jordany@bu.edu), 09/27/2026
# Description: Class-based views for the mini_insta app to list all Instagram user profiles and view individual profile details.

from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Profile

class ProfileListView(ListView):
  """Display a list of all Instagram user profiles in the database."""
  
  # retrieve objects of type Profile from the database
  model = Profile
  template_name = 'mini_insta/show_all_profiles.html'
  # variable name in template context
  context_object_name = 'profiles'
    
class ProfileDetailView(DetailView):
  """Display detailed profile information for a single user profile."""
  
  model = Profile
  template_name = 'mini_insta/show_profile.html'
  context_object_name = 'profile'