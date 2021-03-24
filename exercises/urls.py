from django.urls import path

from .views import *

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('exercises', exercises, name='exercises'),
    path('exercises/orthoepy', orthoepy, name='orthoepy'),
    path('exercises/spelling', spelling, name='spelling'),
    path('exercises/punctuation', punctuation, name='punctuation'),
]