# File: forms.py
# Author: Jordan Yin (jordany@bu.edu), 10/02/2026
# Description: Define the form used to create a new Post.

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
  """Collect the caption needed to create a new Post."""
  
  class Meta:
    """Associate this form with the Post model."""

    model = Post
    fields = ['caption']
    
class UpdateProfileForm(forms.ModelForm):
  '''A form to handle an update to a Profile'''
  
  class Meta:
    '''associate this form with the Profile model; select fields.'''
    model = Profile
    fields = ['display_name', 'bio_text', 'profile_image_url']  # which fields from model should we use

class UpdatePostForm(forms.ModelForm):
  """A form to handle the update to an existing Post."""
  
  class Meta:
    """Associate this form with the Post model."""
    model = Post
    fields = ['caption']