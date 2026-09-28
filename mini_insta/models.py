from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Model to hold Instagram user profile data'''
    # data attributes of a Article:
    username = models.TextField(blank=False)
    display_name = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True)
    # Should I make bio blank = True?
    bio_text = models.TextField(blank=False)
    # Should join date be actual join date or just auto when created?
    join_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        '''Return a string representation of this Profile object.'''
        return f'{self.username} by {self.display_name}'