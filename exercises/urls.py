from django.urls import path
from django.conf.urls import url

from .views import *

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('exercises', exercises, name='exercises'),
    path('exercises/orthoepy', orthoepy_page, name='orthoepy'),
    path('exercises/spelling', spelling_page, name='spelling'),
    path('exercises/punctuation', punctuation_page, name='punctuation'),
    url(r'exercises/end', practice_end),
]