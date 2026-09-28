# File: models.py
# Author: Jordan Yin (jordany@bu.edu), 09/27/2026
# Description: Database model definition for user profiles in the mini_insta application.

from django.db import models

class Profile(models.Model):
    """Model representing an Instagram user profile."""
    
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