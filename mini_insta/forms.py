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