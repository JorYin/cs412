# File: views.py
# Author: Jordan Yin (jordany@bu.edu), 09/27/2026
# Description: Class-based views for the mini_insta app to list all Instagram user profiles and view individual profile details.

from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Profile, Post, Photo
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm
from django.urls import reverse

# Auth
from django.contrib.auth.mixins import LoginRequiredMixin

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
  
class ProfileDetailViewAuth(LoginRequiredMixin, DetailView):
  """Display detailed information for one user profile."""
  
  model = Profile
  template_name = 'mini_insta/show_profile.html'
  context_object_name = 'profile'

  def get_login_url(self):
    """Return the URL for the Mini Insta login page."""
    return reverse('mini_insta_login')

  def get_object(self):
    """Return the profile associated with the currently logged-in user."""
    return Profile.objects.get(user=self.request.user)

class ShowFollowersDetailView(DetailView):
  """Display the profiles following a selected profile."""

  model = Profile
  template_name = 'mini_insta/show_followers.html'
  context_object_name = 'profile'

class ShowFollowingDetailView(DetailView):
  """Display the profiles followed by a selected profile."""

  model = Profile
  template_name = 'mini_insta/show_following.html'
  context_object_name = 'profile'

class PostDetailView(DetailView):
  """Display detailed information for one user's post."""
  
  model = Post
  template_name = 'mini_insta/show_post.html'
  context_object_name = 'post'

  def get_context_data(self, **kwargs):
    """Add the post owner's profile for navigation links."""
    context = super().get_context_data(**kwargs)
    context['profile'] = self.object.profile
    return context
  
class CreatePostView(LoginRequiredMixin, CreateView):
  """Create a post and its related photo for a selected profile."""
  
  form_class = CreatePostForm
  template_name = 'mini_insta/create_post_form.html'

  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login') 
  
  def get_context_data(self):
    """Add the profile associated with the create-post URL to the context."""

    # Begin with the context variables supplied by CreateView.
    context = super().get_context_data()
    
    # Use the profile primary key supplied by the URL to find the owner.
    profile = Profile.objects.get(user=self.request.user)
    
    # Make the profile available to the form template and its URL tags.
    context['profile'] = profile
    return context

  def form_valid(self, form):
    """Attach the profile, save the post, and create its related photo."""

    # Collect every uploaded file from the multipart form submission.
    image_files = self.request.FILES.getlist('files')
    
    # Find the profile identified by the primary key in the URL.
    profile = Profile.objects.get(user=self.request.user)
    
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
  
class UpdateProfileView(LoginRequiredMixin, UpdateView):
  """Display and process the form used to update a Profile."""
  
  model = Profile
  form_class = UpdateProfileForm
  template_name = "mini_insta/update_profile_form.html"
  
  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login')
  
  def get_object(self):
    """Return the profile associated with the currently logged-in user."""
    return Profile.objects.get(user=self.request.user)
  
  def form_valid(self, form):
      """Save a valid profile update."""
      return super().form_valid(form)
    
# Post delete ownership question
class DeletePostView(LoginRequiredMixin, DeleteView):
  """Confirm and delete a post."""

  template_name = "mini_insta/delete_post_form.html"
  model = Post
  context_object_name = 'post'
  
  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login') 

  def get_context_data(self, **kwargs):
    """Add the post owner's profile to the delete confirmation context."""
    
    context = super().get_context_data(**kwargs)
    context['profile'] = self.object.profile
    return context
  
  def get_success_url(self):
    """Return to the profile that owned the deleted post."""
    return reverse('show_profile', kwargs={'pk': self.object.profile.pk})

# Post update ownership question
class UpdatePostView(LoginRequiredMixin, UpdateView):
  """Update an existing post."""
  
  model = Post
  form_class = UpdatePostForm
  template_name = "mini_insta/update_post_form.html"
  context_object_name = 'post'

  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login') 
  
  def get_success_url(self):
    """Return to the post detail page after updating."""
    return reverse('show_post', kwargs={'pk': self.object.pk})
  
class ShowFeedView(LoginRequiredMixin, DetailView):
  """Display the personalized post feed for a Profile."""
  
  model = Profile
  template_name = "mini_insta/show_feed.html"
  context_object_name = 'profile'

  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login') 
  
  def get_object(self):
    """Return the profile associated with the currently logged-in user."""
    return Profile.objects.get(user=self.request.user)
  
class SearchView(LoginRequiredMixin, ListView):
  """Search post captions and profile information."""
  
  model = Post
  template_name = 'mini_insta/search_results.html'

  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login') 
  
  def get_object(self):
    """Return the profile associated with the currently logged-in user."""
    return Profile.objects.get(user=self.request.user)
    
  def dispatch(self, request, *args, **kwargs):
    """Display the search form until a query is submitted."""
    
    profile = Profile.objects.get(user=self.request.user)
    query = request.GET.get('query')

    if query is None:
      return render(
          request,
          'mini_insta/search.html',
          {'profile': profile}
      )
      
    return super().dispatch(request, *args, **kwargs)
    
  def get_queryset(self):
    """Return posts whose captions contain the submitted query."""
    
    query = self.request.GET.get('query').strip()
    return Post.objects.filter(caption__contains = query)
    
  def get_context_data(self, **kwargs):
    """Add the searching profile and matching profiles to the context."""
    
    context = super().get_context_data(**kwargs)
    
    profile = Profile.objects.get(user=self.request.user)
    query = self.request.GET.get('query').strip()
    
    context['profile'] = profile
    context['query'] = query
    context['posts'] = self.get_queryset()
    context['profiles'] = Profile.objects.filter(
      Q(username__contains=query) |
      Q(display_name__contains=query) |
      Q(bio_text__contains=query)
    )

    return context