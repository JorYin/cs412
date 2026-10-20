# File: views.py
# Author: Jordan Yin (jordany@bu.edu), 09/27/2026
# Description: Class-based views for the mini_insta app to list all Instagram user profiles and view individual profile details.

from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Q
from .models import *
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm, CreateProfileForm
from django.urls import reverse

# Auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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

  def get_context_data(self, **kwargs):
    """Add whether the logged-in profile follows the displayed profile."""
    context = super().get_context_data(**kwargs)
    context['is_following'] = False

    if self.request.user.is_authenticated:
      logged_in_profile = Profile.objects.get(user=self.request.user)

      context['is_following'] = Follow.objects.filter(
        profile=self.object,
        follower_profile=logged_in_profile
      ).exists()

    return context
  
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
    """Add the post owner and the logged-in user's like status."""
    context = super().get_context_data(**kwargs)
    context['profile'] = self.object.profile
    
    # Start with no like so logged-out visitors cannot see an active like state.
    context['is_liked'] = False

    # Check the relationship only when a Django user is authenticated.
    if self.request.user.is_authenticated:
      logged_in_profile = Profile.objects.get(user=self.request.user)

      # Match both the displayed post and the logged-in profile.
      context['is_liked'] = Like.objects.filter(
        post=self.object,
        profile=logged_in_profile
      ).exists()
      
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

  def get_context_data(self, **kwargs):
    """Add the IDs of posts liked by the logged-in profile."""
    context = super().get_context_data(**kwargs)

    # Find the profile that owns the current authenticated session.
    if self.request.user.is_authenticated:
      logged_in_profile = Profile.objects.get(user=self.request.user)

    # Use post IDs so the template can determine each feed post's like state.
    context['liked_post_ids'] = Like.objects.filter(
      profile=logged_in_profile
    ).values_list('post_id', flat=True)
      
    return context
  
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
  
class CreateProfileView(CreateView):
  """Create a Django User and its associated Profile."""

  model = Profile
  form_class = CreateProfileForm
  template_name = 'mini_insta/create_profile_form.html'

  def get_context_data(self, **kwargs):
    """Add the UserCreationForm to the profile form context."""
    context = super().get_context_data(**kwargs)
    context['user_form'] = UserCreationForm()
    return context
  
  def form_valid(self, form):
    """Create the User, log them in, and attach them to the Profile."""
    user_form = UserCreationForm(self.request.POST)

    # Should there be validation?

    user = user_form.save()

    login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

    form.instance.user = user

    return super().form_valid(form)
  
class FollowProfileView(LoginRequiredMixin, TemplateView):
  """Create a Follow relationship with another profile."""

  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login') 
  
  def dispatch(self, request, *args, **kwargs):
    """Create a follow relationship for a POST request."""
    
    # Identify the profile performing the action and the target profile.
    if request.POST:
      logged_in_profile = Profile.objects.get(user=self.request.user)
      pk = self.kwargs['pk']
      target_profile = Profile.objects.get(pk=pk)
      
      # Prevent a profile from creating a relationship with itself.
      if logged_in_profile != target_profile:
        # Reuse an existing relationship instead of creating duplicates.
        Follow.objects.get_or_create(
          profile=target_profile,
          follower_profile=logged_in_profile
      )
      
      return render(
        request,
        'mini_insta/show_profile.html',
        {
            'profile': target_profile,
            'is_following': True,
        }
      )
      
    return super().dispatch(request, *args, **kwargs)

class DeleteFollowView(LoginRequiredMixin, TemplateView):
  """Delete a Follow relationship with another profile."""

  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login') 

  def dispatch(self, request, *args, **kwargs):
    """Delete a follow relationship for a POST request."""
    
    # Identify the profile performing the action and the target profile.
    if request.POST:
      logged_in_profile = Profile.objects.get(user=self.request.user)
      pk = self.kwargs['pk']
      target_profile = Profile.objects.get(pk=pk)
      
      # Delete only the relationship between these two specific profiles.
      Follow.objects.filter(
          profile=target_profile,
          follower_profile=logged_in_profile
      ).delete()
      
      return render(
        request,
        'mini_insta/show_profile.html',
        {
            'profile': target_profile,
            'is_following': False,
        }
      )
      
    return super().dispatch(request, *args, **kwargs)
  
class LikePostView(LoginRequiredMixin, TemplateView):
  """Create a Like for another profile's post."""

  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login')
  
  def dispatch(self, request, *args, **kwargs):
    """Create a like relationship for a POST request."""
    
    # Identify the profile performing the action and the target post.
    if request.POST:
      logged_in_profile = Profile.objects.get(user=self.request.user)
      pk = self.kwargs['pk']
      target_post = Post.objects.get(pk=pk)
      
      # Prevent a profile from liking a post it owns.
      if logged_in_profile != target_post.profile:
        # Reuse an existing like instead of creating duplicates.
        Like.objects.get_or_create(
            post=target_post,
            profile=logged_in_profile
        )
      
      return render(
          request,
          'mini_insta/show_post.html',
          {
              'post': target_post,
              'profile': target_post.profile,
              'is_liked': True,
          }
      )
      
    return super().dispatch(request, *args, **kwargs)

class DeleteLikeView(LoginRequiredMixin, TemplateView):
  """Delete a Like from another profile's post."""

  def get_login_url(self) -> str:
    """return the URL required for login"""
    return reverse('mini_insta_login') 

  def dispatch(self, request, *args, **kwargs):
    """Delete a like relationship for a POST request."""
    
    # Identify the profile performing the action and the target post.
    if request.POST:
      logged_in_profile = Profile.objects.get(user=self.request.user)
      pk = self.kwargs['pk']
      target_post = Post.objects.get(pk=pk)
      
      # Delete only the like belonging to this profile and post.
      Like.objects.filter(
          post=target_post,
          profile=logged_in_profile
      ).delete()

    return render(
        request,
        'mini_insta/show_post.html',
        {
            'post': target_post,
            'profile': target_post.profile,
            'is_liked': False,
        }
    )
      
    return super().dispatch(request, *args, **kwargs)