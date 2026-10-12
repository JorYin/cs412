# File: urls.py
# Author: Jordan Yin (jordany@bu.edu), 09/27/2026
# Description: URL pattern routing configuration mapping URL endpoints to class-based views for the mini_insta app.

from django.urls import path
from .views import *

# URL patterns specific to the mini_insta app:
urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name="show_profile"),
    path('profile/<int:pk>/create_post', CreatePostView.as_view(), name="create_post"),
    path('post/<int:pk>', PostDetailView.as_view(), name="show_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name="update_post"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name="show_followers"),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name="show_following"),
    path('profile/<int:pk>/feed', ShowFeedView.as_view(), name="show_feed_view"),
    path('profile/<int:pk>/search', SearchView.as_view(), name="search_view")
]