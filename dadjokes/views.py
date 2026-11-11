# File: views.py
# Author: Jordan Yin (jordany@bu.edu), 11/10/2026
# Description: Class-based views for displaying Dad Jokes and pictures.

from django.shortcuts import render

# Create your views here.
from .models import *
from django.views.generic import ListView, DetailView

import random

# API
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# API Views
class RandomJokeAPI(APIView):
  '''Return one randomly selected joke as JSON.'''
  def get(self, request):
    joke = random.choice(Joke.objects.all())
    serializer_class = JokeSerializer(joke)
    return Response(serializer_class.data)

class JokeListCreateAPI(generics.ListCreateAPIView):
  '''List all jokes and create a new joke.'''
  queryset = Joke.objects.all()
  serializer_class = JokeSerializer

class JokeDetailAPI(generics.RetrieveAPIView):
  '''Return one joke selected by its primary key as JSON.'''
  queryset = Joke.objects.all()
  serializer_class = JokeSerializer

class PictureListAPI(generics.ListAPIView):
  '''List all pictures as JSON.'''
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer

class PictureDetailAPI(generics.RetrieveAPIView):
  '''Return one picture selected by its primary key as JSON.'''
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer

class RandomPictureAPI(APIView):
  '''Return one randomly selected picture as JSON.'''
  def get(self, request):
    picture = random.choice(Picture.objects.all())
    serializer_class = PictureSerializer(picture)
    return Response(serializer_class.data)

# Page Views
class RandomJoke(DetailView):
    '''Display one randomly selected joke and picture.'''
    model = Joke
    template_name = 'dadjokes/home.html'
    context_object_name = 'joke'
    
    # Pick one joke at random.
    def get_object(self):
      '''Return one Joke object selected at random.'''
      all_jokes = Joke.objects.all()
      return random.choice(all_jokes)
    
    def get_context_data(self, **kwargs):
      '''Add one randomly selected picture to the template context.'''
      
      context = super().get_context_data(**kwargs)
      all_pictures = Picture.objects.all()
      context['picture'] = random.choice(all_pictures)
      return context

class AllJokes(ListView):
  '''Display all jokes without pictures.'''
  model = Joke
  template_name = 'dadjokes/jokes.html'
  context_object_name = 'jokes'

class AllPictures(ListView):
  '''Display all pictures without jokes.'''
  model = Picture
  template_name = 'dadjokes/pictures.html'
  context_object_name = 'pictures'
  
class JokeDetail(DetailView):
  '''Display one joke selected by its primary key.'''
  model = Joke
  template_name = 'dadjokes/joke.html'
  context_object_name = 'joke'

class PictureDetail(DetailView):
  '''Display one picture selected by its primary key.'''
  model = Picture
  template_name = 'dadjokes/picture.html'
  context_object_name = 'picture'