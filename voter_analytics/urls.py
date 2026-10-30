# File: urls.py
# Author: Jordan Yin (jordany@bu.edu), 10/30/2026
# Description: URL patterns for voter list, detail, and graph pages.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.VoterListView.as_view(), name='voters'),
    path('voters', views.VoterListView.as_view(), name='voter_list'),
    path('voter/<int:pk>', views.VoterDetailView.as_view(), name='voter'),
    path('graphs', views.VoterGraphsView.as_view(), name='graphs'),
]