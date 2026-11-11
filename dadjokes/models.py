# File: models.py
# Author: Jordan Yin (jordany@bu.edu), 11/10/2026
# Description: Data models for jokes and pictures.

from django.db import models

# Create your models here.

class Joke(models.Model):
    '''Store a joke, its contributor, and when it was published.'''
    
    joke = models.TextField(blank=False)
    contributor = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        '''Return the joke text.'''
        return self.joke
      
class Picture(models.Model):
    '''Store a picture URL, its contributor, and when it was published.'''
    
    image_url = models.URLField(blank=False)
    contributor = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        '''Return the picture URL.'''
        return self.image_url