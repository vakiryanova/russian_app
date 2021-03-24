from django.shortcuts import render
from .models import *
from .serializers import *

# Create your views here.

def landing_page(request):
	return render(request, 'front/about.html')

def exercises(request):
	return render(request, 'front/tests.html')

def orthoepy(request):
	words = Orthoepy.objects.all()
	words_serialized = OrthoepySerializer(words, many=True)
	return render(request, 'front/orthoepy.html', {'data': words_serialized.data})

def spelling(request):
	return render(request, 'front/spelling.html')

def punctuation(request):
	return render(request, 'front/punctuation.html')