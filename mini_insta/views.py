# File: views.py
# Author: Jordan Yin (jordany@bu.edu), 09/27/2026
# Description: Class-based views for the mini_insta app to list all Instagram user profiles and view individual profile details.

from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Profile, Post, Photo
from .forms import CreatePostForm
from django.urls import reverse

class ProfileListView(ListView):
  """Display all Instagram user profiles in the database."""
  
  # Retrieve objects of type Profile from the database
  model = Profile
  template_name = 'mini_insta/show_all_profiles.html'
  # Variable name in template context
  context_object_name = 'profiles'
    
class ProfileDetailView(DetailView):
  """Display detailed information for one user profile."""
  
  model = Profile
  template_name = 'mini_insta/show_profile.html'
  context_object_name = 'profile'

class PostDetailView(DetailView):
  """Display detailed information for one user's post."""
  
  model = Post
  template_name = 'mini_insta/show_post.html'
  context_object_name = 'post'
  
class CreatePostView(CreateView):
  """Create a post and its related photo for a selected profile."""
  
  form_class = CreatePostForm
  template_name = 'mini_insta/create_post_form.html'
  
  def get_context_data(self):
    """Add the profile associated with the create-post URL to the context."""

    # Begin with the context variables supplied by CreateView.
    context = super().get_context_data()
    
    # Use the profile primary key supplied by the URL to find the owner.
    pk = self.kwargs['pk']
    profile = Profile.objects.get(pk=pk)
    
    # Make the profile available to the form template and its URL tags.
    context['profile'] = profile
    return context

  def form_valid(self, form):
    """Attach the profile, save the post, and create its related photo."""

    # Collect every uploaded file from the multipart form submission.
    image_files = self.request.FILES.getlist('files')
    
    # Find the profile identified by the primary key in the URL.
    pk = self.kwargs['pk']
    profile = Profile.objects.get(pk=pk)
    
    # Set the profile before CreateView saves the Post.
    form.instance.profile = profile
    
    # Save the Post and prepare the response that redirects to its detail page.
    response = super().form_valid(form)
    
    # Create one Photo record for each uploaded file after the Post is saved.
    for image_file in image_files:
      Photo.objects.create(
          post=self.object,
          image_file=image_file
      )
    
    return response

  def get_success_url(self):
    """Return the detail-page URL for the newly created post."""

    # Reverse the post detail route using the saved post's primary key.
    return reverse('show_post', kwargs={'pk': self.object.pk})