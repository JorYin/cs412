# File: urls.py
# Author: Jordan Yin (jordany@bu.edu), 11/10/2026
# Description: URL patterns for Dad Jokes pages.

from django.urls import path
from .views import *

urlpatterns = [
    path('', RandomJoke.as_view(), name='one_joke'),
    path('random', RandomJoke.as_view(), name='random_joke_and_picture'),
    path('jokes', AllJokes.as_view(), name='jokes_no_picture'),
    path('joke/<int:pk>', JokeDetail.as_view(), name='joke_by_pk'),
    path('pictures', AllPictures.as_view(), name='pictures_no_jokes'),
    path('picture/<int:pk>', PictureDetail.as_view(), name='picture_by_pk'),
    
    # API URLS
    path('api/', RandomJokeAPI.as_view(), name='api_random_joke_base'),
    path('api/random', RandomJokeAPI.as_view(), name='api_random_joke'),
    path('api/jokes', JokeListCreateAPI.as_view(), name='api_jokes'),
    path('api/joke/<int:pk>', JokeDetailAPI.as_view(), name='api_joke_by_pk'),
    path('api/pictures', PictureListAPI.as_view(), name='api_pictures'),
    path('api/picture/<int:pk>', PictureDetailAPI.as_view(), name='api_picture_by_pk'),
    path('api/random_picture', RandomPictureAPI.as_view(), name='api_random_picture'),
]