from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
import json

models_ = {
	'Orthoepy': Orthoepy,
	'Spelling': Spelling,
	'Punctuation': Punctuation,
}

# Create your views here.

def landing_page(request):
	return render(request, 'front/about.html')

def exercises(request):
	return render(request, 'front/tests.html')

def orthoepy_page(request):
	words = Orthoepy.objects.all()
	words_serialized = OrthoepySerializer(words, many=True)
	return render(request, 'front/orthoepy.html', {'data': words_serialized.data})

def spelling_page(request):
	words = Spelling.objects.all()
	words_serialized = SpellingSerializer(words, many=True)
	return render(request, 'front/spelling.html', {'data': words_serialized.data})

def punctuation_page(request):
	words = Punctuation.objects.all()
	words_serialized = PunctuationSerializer(words, many=True)
	return render(request, 'front/punctuation.html', {'data': words_serialized.data})

@csrf_exempt
def practice_end(request):
	res = json.loads(request.body)
	model_name = res['model_name']
	data = res['data']
	for item in data:
		word = models_[model_name].objects.get(id=item['id'])
		word.total_count += 1
		if item['correct'] == False:
			word.mistakes += 1 
		word.save()
	return render(request, 'front/tests.html')
	# redirect(request, exercises) 