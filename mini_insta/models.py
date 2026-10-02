# File: models.py
# Author: Jordan Yin (jordany@bu.edu), 09/27/2026
# Description: Database model definition for user profiles in the mini_insta application.

from django.db import models

class Profile(models.Model):
    """Represent an Instagram user profile."""
    
    # data attributes for a user profile:
    username = models.TextField(blank=False)
    display_name = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True)
    
    # Should I make bio blank = True?
    bio_text = models.TextField(blank=False)
    
    # Should join date be actual join date or just auto when created?
    join_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a string representation of the Profile object."""
        return f'{self.username} by {self.display_name}'

    def get_all_posts(self):
        """Return this profile's posts in reverse chronological order."""

        # Retrieve only posts belonging to this profile and show newest first.
        posts = Post.objects.filter(profile=self).order_by('-timestamp')
        return posts
    
class Post(models.Model):
    """Represent a post created by an Instagram user profile."""
    
    # data attributes for a user post:
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a string representation of the Post for that Profile"""
        return f'{self.profile} post at {self.timestamp}'
    
    def get_all_photos(self):
        """Return all photos associated with this post."""

        # Retrieve every Photo whose foreign key points to this post.
        photos = Photo.objects.filter(post=self)
        return photos

class Photo(models.Model):
    """Represent a photo associated with an Instagram post."""
    
    # data attributes for Photos:
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a string representation of this post photo."""
        return f'{self.post} at {self.timestamp}'