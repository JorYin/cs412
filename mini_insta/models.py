# File: models.py
# Author: Jordan Yin (jordany@bu.edu), 09/27/2026
# Description: Database model definition for user profiles in the mini_insta application.

from django.db import models

class Profile(models.Model):
    """Represent an Instagram user profile."""
    
    # Data attributes for a user profile:
    username = models.TextField(blank=False)
    display_name = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True)
    
    bio_text = models.TextField(blank=False)
    
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
    
    # Data attributes for a user post:
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a string representation of this post and its profile."""
        return f'{self.profile} post at {self.timestamp}'
    
    def get_all_photos(self):
        """Return all photos associated with this post."""

        # Retrieve every Photo whose foreign key points to this post.
        photos = Photo.objects.filter(post=self)
        return photos

class Photo(models.Model):
    """Represent a photo associated with an Instagram post."""
    
    # Data attributes for a photo:
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def get_image_url(self):
        """Return the URL for this photo's image."""

        # Prefer the existing public URL for backwards compatibility.
        if self.image_url:
            return self.image_url

        # If there is no public URL, use the URL for the uploaded image file.
        if self.image_file:
            return self.image_file.url

        return ''
    
    def __str__(self):
        """Return a string describing the photo and its storage location."""

        # Identify photos that still use an external image URL.
        if self.image_url:
            return f'{self.post} photo from URL: {self.image_url}'

        # Identify photos stored as uploaded files in the media directory.
        if self.image_file:
            return f'{self.post} photo from file: {self.image_file.name}'

        return f'{self.post} photo with no image'