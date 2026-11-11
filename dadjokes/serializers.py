# File: serializers.py
# Author: Jordan Yin (jordany@bu.edu), 11/10/2026
# Description: REST API serializers for Dad Jokes models.

from rest_framework import serializers
from .models import Joke, Picture

class JokeSerializer(serializers.ModelSerializer):
    '''Serialize Joke objects for the REST API.'''
    
    class Meta:
        model = Joke
        fields = ['id', 'joke', 'contributor', 'published']

    def create(self, validated_data):
        '''Create and save a Joke from validated API data.'''
        return Joke.objects.create(**validated_data)
      
class PictureSerializer(serializers.ModelSerializer):
    '''Serialize Picture objects for the REST API.'''
    
    class Meta:
        model = Picture
        fields = ['id', 'image_url', 'contributor', 'published']